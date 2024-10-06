prompt_template = """
    You are an expert at creating job interview questions based on any kind of professional material.
    Your goal is to prepare a candidate for interviews in various fields.
    You do this by asking relevant, field-specific questions about the text below:

    ------------
    {text}
    ------------

    Create five to ten interview questions and provide only the questions, without any additional explanation or context. Separate each question with a newline.

    QUESTIONS:
    """


refine_template = ("""
    You are an expert at refining job interview questions based on any professional material.
    Your goal is to ensure the questions are well-suited for job interviews across different fields.
    We have received some interview questions to a certain extent: {existing_answer}.
    We have the option to refine the existing questions or add new ones.
    (only if necessary) with some more context below.
    ------------
    {text}
    ------------

    Refine or add to the original questions as needed, but provide only the questions, without any additional explanation or context. Separate each question with a newline.

    QUESTIONS:
    """
)