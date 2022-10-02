low_risk_generic_answer = """
The described AI use case is likely to be classified as low-risk according to the EU AI Act. However, please seek further legal advice.

The list of aspects that make a system high-risk

1. Biometric identification & categorisation of natural persons
2. Management and operation of critical infrastructure
3. Education and vocational training
4. Employment, workers management and access to self-
employment:
5. Access to and enjoyment of essential private services
and public services and benefits
6. Law enforcement
7. Migration, asylum and border control management
8. Administration of justice and democratic processes

9. AI as a safety component of regulated products such as but not limited to: Machinery Watercraft, Equipment for explosive atmospheres, Radio equipment, In vitro diagnostic medical devices, Cableway installations, Toys, Lifts, Personal protection equipment, Pressure equipment, Appliances burning fuels, Medical devices """

prohibited_dict = {
    1: """
        an AI system that deploys
        subliminal techniques beyond a person’s consciousness with the objective to or the
        effect of materially distorting a person’s behaviour in a manner that
        causes or is reasonably likely to cause that person or another person physical or
        psychological harm
        """,
    2: """
        an AI system that exploits
        any of the vulnerabilities of a specific group of persons due to their age, disability or social or economic situation, with the objective to or the
        effect of materially distorting the behaviour of a person pertaining to that
        group in a manner that causes or is reasonably likely to cause that person or another
        person physical or psychological harm
    """,
    3: """
        AI systems for the evaluation or classification 
        of natural persons over a certain period of time based on their social behaviour or
        known or predicted personal or personality characteristics, with the social score
        leading to either or both of the following:
        (i) detrimental or unfavourable treatment of certain natural persons or
        groups thereof in social contexts which are unrelated to the contexts in which
        the data was originally generated or collected;
        (ii) detrimental or unfavourable treatment of certain natural persons or
        groups thereof that is unjustified or disproportionate to their social behaviour
        or its gravity;
    """,
    4: """
        the use of ‘real-time’ biometric identification systems in publicly accessible
        spaces by law enforcement authorities or on their behalf for the purpose of law
        enforcement, unless and in as far as such use is strictly necessary for one of the
        following objectives:
        (i) the targeted search for specific potential victims of crime;
        (ii) the prevention of a specific and substantial threat to the critical
        infrastructure, life, health or physical safety of natural persons or the
        prevention of a terrorist attacks; 
    """,
    5: """
        the, localisation, or identification of a natural person
        for the purposes of conducting a criminal investigation, prosecution or
        executing a criminal penalty for offences referred to in Article 2(2) of Council Framework
        Decision 2002/584/JHA33 and punishable in the Member State concerned by a
        custodial sentence or a detention order for a maximum period of at least three
        years, or other specific offences punishable in the Member State
        concerned by a custodial sentence or a detention order for a maximum
        period of at least five years, as determined by the law of that Member State.
    """
}


high_risk_dict = {
    1: """
    The use case seems to “use biometric identification & categorisation of natural persons”. This could include using AI systems to verify the authenticity of travel documents and determine the right to migration or asylum at border control. There is a risk of these system producing biased results based on physical characteristics.

    Required internal assessment check-list for high-risk AI systems
        1. Establish a risk management system
        2. Write up-to-date technical documentation 
        3. Fulfil requirements on used training, testing and validation data sets 
        4. Achieve appropriate level of accuracy, robustness and cybersecurity
        5. Perform conformity assessment of the system
        6. Register the system to the EU’s database that is accessible to the public
        7. Keep record when the system is in use
        8. Maintain post-market monitoring and report serious incidents and malfunctioning

    Suggested tools:

    Microsoft Fairlearn Open source toolkit that empowers data scientists and developers to assess and improve the fairness of their AI systems. Fairlearn has two components: an interactive visualization dashboard and unfairness mitigation algorithms.

    VIRT-EU Service Package Capacity-building material and practical resources to help develop ethically-informed AI systems, based on three different ethical frameworks: virtue ethics, care ethics and capabilities approach.

    Google What-if Tool What-If Tool let users analyze an ML model without writing code. The What-If Tool has a large set of features, including visualizing your dataset automatically using Facets, the ability to manually edit examples from your dataset and see the effect of those changes, and automatic generation of partial dependence plots which show how the model’s predictions change as any single feature is changed.
    """,
    2: """
    The use case seems to involve the “management and operation of critical infrastructure” including road traffic, water, heat, gas, electricity. These systems have the capacity put people’s life and health at risk.

    Required internal assessment check-list for high-risk AI systems
        1. Establish a risk management system
        2. Write up-to-date technical documentation 
        3. Fulfil requirements on used training, testing and validation data sets 
        4. Achieve appropriate level of accuracy, robustness and cybersecurity
        5. Perform conformity assessment of the system
        6. Register the system to the EU’s database that is accessible to the public
        7. Keep record when the system is in use
        8. Maintain post-market monitoring and report serious incidents and malfunctioning

    Suggested tools:

    Microsoft Fairlearn Open source toolkit that empowers data scientists and developers to assess and improve the fairness of their AI systems. Fairlearn has two components: an interactive visualization dashboard and unfairness mitigation algorithms.

    AI Trust Standard & Label The AI Trust Standard & Label describes the characteristics of an AI product with regards to: Transparency, Accountability, Privacy, Fairness and Reliability.

    Evaluate Library and Evaluation on the Hub (Hugging Face) The Evaluation on the Hub platform extends the Evaluate library to a free service model: anyone can evaluate any model on any dataset using any compatible metric, without requiring any code. 
    """,
    3: "Education and vocational training",
    4: "Employment, workers management and access to self-employment",
    5: "Access to and enjoyment of essential private services and public services and benefits",
    6: "Law enforcement",
    7: "Migration, asylum and border control management",
    8: "Administration of justice and democratic processes"
}
