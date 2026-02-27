import random
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# FastAPI app
app = FastAPI()

# CORS: allow local file:// frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Response model
class ReviewResponse(BaseModel):
    background: str
    key_points: str
    research_gaps: str
    future_directions: str

# Endpoint: accepts any JSON, reads body["topic"]
@app.post("/generate_review", response_model=ReviewResponse)
async def generate_review(request: Request):
    body = await request.json()
    topic = (body.get("topic") or "").strip() or "the given research area"

    bg_templates = [
        (
            f"- This literature review focuses on {topic}.\n"
            f"- Researchers have explored this area from multiple perspectives, "
            f"including methodology, applications, and limitations.\n"
            f"- Recent advances in AI and data availability have accelerated work in this domain.\n"
        ),
        (
            f"- The primary scope of this review is {topic}.\n"
            f"- Work in this space spans theory, practical systems, and real-world case studies.\n"
            f"- Growing interest in AI and automation has led to a rapid increase in publications.\n"
        ),
        (
            f"- This review examines current research on {topic}.\n"
            f"- Studies cover a mix of conceptual frameworks, empirical analyses, and tools.\n"
            f"- The topic has gained significance as data and computational resources have expanded.\n"
        ),
        (
            f"- This review surveys how {topic} is being adopted in real-world settings.\n"
            f"- Contributions range from early conceptual work to mature, deployed systems.\n"
            f"- The topic has become central as AI capabilities and data volumes have grown.\n"
        ),
        (
            f"- We provide a focused overview of research on {topic}.\n"
            f"- The literature spans multiple disciplines, reflecting the cross-cutting nature of this topic.\n"
            f"- Interest has accelerated in recent years due to practical demand and better tooling.\n"
        ),
        (
            f"- This survey synthesises recent work on {topic}.\n"
            f"- Prior studies investigate both theoretical foundations and applied systems.\n"
            f"- As datasets and compute have scaled, the research landscape has evolved rapidly.\n"
        ),
        (
            f"- In this review, we outline the current state of research on {topic}.\n"
            f"- The field includes contributions from academia, industry, and open-source communities.\n"
            f"- The topic has moved from exploratory studies to more mature, production-grade deployments.\n"
        ),
        (
            f"- We examine how {topic} has emerged as a key theme in recent literature.\n"
            f"- Existing work spans methodological advances, application-focused studies, and position papers.\n"
            f"- This review aims to organise these contributions into a coherent narrative.\n"
        ),
    ]

    key_templates = [
        (
            "- Existing work can be grouped into three broad themes:\n"
            "  1) Foundational theories and models.\n"
            "  2) Practical applications and case studies.\n"
            "  3) Tools, frameworks, and evaluation benchmarks.\n"
            "- Many studies emphasize performance, but fewer discuss real-world deployment challenges.\n"
        ),
        (
            "- Prior research tends to organise around three pillars:\n"
            "  1) Core algorithms and architectures.\n"
            "  2) Domain-specific applications and workflows.\n"
            "  3) Infrastructure, tooling, and integration with existing systems.\n"
            "- Several works report strong results on benchmarks, yet external validity is often limited.\n"
        ),
        (
            "Existing work can roughly be divided into three strands.\n"
            "- First, core methods and model architectures.\n"
            "- Second, domain-specific applications and pipelines.\n"
            "- Third, tooling and platforms that integrate these models into workflows.\n"
        ),
        (
            "The literature reports a wide variety of use cases.\n"
            "- Some studies focus on small-scale prototypes and user studies.\n"
            "- Others assess scalability, cost, and integration with legacy systems.\n"
            "- A few works reflect on long-term maintenance and governance.\n"
        ),
        (
            "- The body of work reveals recurring patterns across multiple domains.\n"
            "- Many papers centre on improving accuracy, efficiency, or robustness of models.\n"
            "- Fewer contributions analyse organisational impact, user experience, or adoption barriers.\n"
        ),
        (
            "- Across the literature, we observe a split between method-centric and application-centric work.\n"
            "- Method papers refine architectures, training strategies, and optimisation techniques.\n"
            "- Application papers adapt these ideas to specific domains with domain-specific constraints.\n"
        ),
        (
            "- Several surveys and empirical studies attempt to map the space.\n"
            "- Comparative evaluations are available for some settings, but they often cover a narrow subset of methods.\n"
            "- Many niche use cases are documented only through small case studies or technical reports.\n"
        ),
    ]

    gap_templates = [
        (
            "- Limited large-scale empirical evaluations across diverse settings.\n"
            "- Lack of standardised benchmarks and reproducible baselines.\n"
            "- Insufficient focus on fairness, interpretability, and ethical implications.\n"
        ),
        (
            "- Few studies evaluate long-term robustness or real-world adoption barriers.\n"
            "- Methodological choices and datasets are not always documented transparently.\n"
            "- Governance, accountability, and human-in-the-loop aspects remain under-explored.\n"
        ),
        (
            "- Limited analysis of hallucinations and error patterns in high-stakes decisions.\n"
            "- Few works compare AI-assisted workflows against expert-only baselines.\n"
            "- Trade-offs between speed, cost, and evidence quality are rarely quantified.\n"
        ),
        (
            "- Cross-domain comparisons are still rare, which makes generalisation difficult.\n"
            "- Negative results and failed deployments are under-reported in the literature.\n"
            "- User experience, training needs, and collaboration patterns receive limited attention.\n"
        ),
        (
            "- Many studies assume idealised conditions and well-curated datasets.\n"
            "- The impact of organisational culture and regulatory constraints is seldom analysed.\n"
            "- Interdisciplinary perspectives from social sciences and HCI are still emerging.\n"
        ),
    ]

    future_templates = [
        (
            "- Building open, reproducible datasets and benchmarks for this topic.\n"
            "- Combining traditional methods with modern AI techniques.\n"
            "- Studying long-term impact, user acceptance, and real-world constraints.\n"
        ),
        (
            "- Developing standardised evaluation protocols that reflect realistic use cases.\n"
            "- Exploring hybrid human–AI workflows rather than fully automated pipelines.\n"
            "- Investigating policy, regulatory, and educational implications of this technology.\n"
        ),
        (
            "- Designing AI-assisted tools that keep human experts in control of critical decisions.\n"
            "- Creating shared benchmarks for factual consistency and hallucination rates.\n"
            "- Examining how these tools change researchers’ behaviour and trust in automation.\n"
        ),
        (
            "- Extending experiments to more diverse domains, datasets, and user groups.\n"
            "- Integrating insights from HCI, ethics, and organisational studies into system design.\n"
            "- Building end-to-end pipelines that are observable, auditable, and maintainable.\n"
        ),
        (
            "- Encouraging open-source reference implementations to lower the barrier to entry.\n"
            "- Co-designing solutions with practitioners to ensure alignment with real workflows.\n"
            "- Tracking the long-term lifecycle of deployed systems, including failure modes.\n"
        ),
    ]

    background = random.choice(bg_templates)
    key_points = random.choice(key_templates)
    research_gaps = random.choice(gap_templates)
    future_directions = random.choice(future_templates)

    return ReviewResponse(
        background=background,
        key_points=key_points,
        research_gaps=research_gaps,
        future_directions=future_directions,
    )

