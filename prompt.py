from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate

prompt = ChatPromptTemplate.from_messages([

SystemMessagePromptTemplate.from_template("""
You are an expert Machine Learning Engineer.

Analyze Random Forest tuning
results using Tree-of-Thought.

1. Promising Hyperparameter Ranges
2. Bias-Variance Analysis
3. Training Time vs Performance
4. Best Configuration
5. Final Justification

Think step-by-step.
"""),

HumanMessagePromptTemplate.from_template("""
{results}
""")
    ])