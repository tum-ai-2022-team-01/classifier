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
    3: """
    The use case seems to involve the applications in educational and vocational settings where the AI system could determine access to education or professional training. There is a risk that these products could produce biased results and could negatively influence the livelihoods of people.

Required internal assessment check-list for high-risk AI systems
1.	Establish a risk management system
2.	Write up-to-date technical documentation 
3.	Fulfil requirements on used training, testing and validation data sets 
4.	Achieve appropriate level of accuracy, robustness and cybersecurity
5.	Perform conformity assessment of the system
6.	Register the system to the EU’s database that is accessible to the public
7.	Keep record when the system is in use
8.	Maintain post-market monitoring and report serious incidents and malfunctioning

Suggested tools:

fairlens FairLens is an open source Python library for automatically discovering bias and measuring fairness in data. The package can be used to quickly identify bias, and provides multiple metrics to measure fairness across a range of sensitive and legally protected characteristics such as age, race and sex.

Microsoft InterpretML Model interpretability helps developers, data scientists and business stakeholders in the organization gain a comprehensive understanding of their machine learning models. It can also be used to debug models, explain predictions and enable auditing to meet compliance with regulatory requirements.

AI Trust Standard & Label The AI Trust Standard & Label describes the characteristics of an AI product with regards to: Transparency, Accountability, Privacy, Fairness and Reliability.

    """,
    4: """
    The use case seems to be related to “employment, workers management and access to self-employment”. There is a risk that these products could produce biased results and could negatively influence the livelihoods of people.

Required internal assessment check-list for high-risk AI systems
1.	Establish a risk management system
2.	Write up-to-date technical documentation 
3.	Fulfil requirements on used training, testing and validation data sets 
4.	Achieve appropriate level of accuracy, robustness and cybersecurity
5.	Perform conformity assessment of the system
6.	Register the system to the EU’s database that is accessible to the public
7.	Keep record when the system is in use
8.	Maintain post-market monitoring and report serious incidents and malfunctioning

Suggested tools:

LinkedIn Fairness Toolkit (LiFT) Open source toolkit to enable measurement of fairness according to a multitude of fairness definitions in large-scale machine learning workflows. 

Microsoft Datasheets for Datasets Tool for documenting the datasets used for training and evaluating machine learning models to increase dataset transparency and facilitate better communication between dataset creators and dataset consumers, and encourage the machine learning community to prioritize transparency and accountability.

Evaluate Library and Evaluation on the Hub (Hugging Face) The Evaluation on the Hub platform extends the Evaluate library to a free service model: anyone can evaluate any model on any dataset using any compatible metric, without requiring any code.

    """,
    5: """
    The use case seems to be related to essential private and public services, including access to financial services such as credit scoring systems. There is a risk that these products could produce biased results and could negatively influence the livelihoods of people. These use cases can also affect children by determining access to education or evaluating students.


Required internal assessment check-list for high-risk AI systems
1.	Establish a risk management system
2.	Write up-to-date technical documentation 
3.	Fulfil requirements on used training, testing and validation data sets 
4.	Achieve appropriate level of accuracy, robustness and cybersecurity
5.	Perform conformity assessment of the system
6.	Register the system to the EU’s database that is accessible to the public
7.	Keep record when the system is in use
8.	Maintain post-market monitoring and report serious incidents and malfunctioning

Suggested tools:
Microsoft InterpretML Model interpretability helps developers, data scientists and business stakeholders in the organization gain a comprehensive understanding of their machine learning models. It can also be used to debug models, explain predictions and enable auditing to meet compliance with regulatory requirements.

VIRT-EU Service Package Capacity-building material and practical resources to help develop ethically-informed AI systems, based on three different ethical frameworks: virtue ethics, care ethics and capabilities approach.

LinkedIn Fairness Toolkit (LiFT) Open source toolkit to enable measurement of fairness according to a multitude of fairness definitions in large-scale machine learning workflows

    """,
    6: """
    The use case seems to be used in law enforcement. There is a risk that these products could produce biased results and could negatively influence the livelihoods of people and cause serious legal issues.


Required internal assessment check-list for high-risk AI systems
1.	Establish a risk management system
2.	Write up-to-date technical documentation 
3.	Fulfil requirements on used training, testing and validation data sets 
4.	Achieve appropriate level of accuracy, robustness and cybersecurity
5.	Perform conformity assessment of the system
6.	Register the system to the EU’s database that is accessible to the public
7.	Keep record when the system is in use
8.	Maintain post-market monitoring and report serious incidents and malfunctioning

Suggested tools:

Model Cards (Hugging Face) Model cards are short documents accompanying trained machine learning (ML) models that provide benchmarked evaluation in a variety of conditions.. Model cards also disclose the context in which models are intended to be used, details of the performance evaluation procedures, and other relevant information. This framework can be used to document any trained ML model. 

fairlens FairLens is an open source Python library for automatically discovering bias and measuring fairness in data. The package can be used to quickly identify bias, and provides multiple metrics to measure fairness across a range of sensitive and legally protected characteristics such as age, race and sex.

Microsoft InterpretML Model interpretability helps developers, data scientists and business stakeholders in the organization gain a comprehensive understanding of their machine learning models. It can also be used to debug models, explain predictions and enable auditing to meet compliance with regulatory requirements.

    """,
    7: """
    The use case seems to be used in the context of “migration, asylum and border control management” There is a risk of these system producing biased and discriminatory results based on physical characteristics.


Required internal assessment check-list for high-risk AI systems
1.	Establish a risk management system
2.	Write up-to-date technical documentation 
3.	Fulfil requirements on used training, testing and validation data sets 
4.	Achieve appropriate level of accuracy, robustness and cybersecurity
5.	Perform conformity assessment of the system
6.	Register the system to the EU’s database that is accessible to the public
7.	Keep record when the system is in use
8.	Maintain post-market monitoring and report serious incidents and malfunctioning

Suggested tools:

Microsoft Datasheets for Datasets Tool for documenting the datasets used for training and evaluating machine learning models to increase dataset transparency and facilitate better communication between dataset creators and dataset consumers, and encourage the machine learning community to prioritize transparency and accountability.

fairlens FairLens is an open source Python library for automatically discovering bias and measuring fairness in data. The package can be used to quickly identify bias, and provides multiple metrics to measure fairness across a range of sensitive and legally protected characteristics such as age, race and sex.

LinkedIn Fairness Toolkit (LiFT) Open source toolkit to enable measurement of fairness according to a multitude of fairness definitions in large-scale machine learning workflows.

    """,
    8: """
    The use case seems to be used for “administration of justice and democratic processes”. Assist in judicial systems such as using AI to research facts and the law carries the risk of producing false legal assumptions during judicial processes and requires constant human supervision.


Required internal assessment check-list for high-risk AI systems
1.	Establish a risk management system
2.	Write up-to-date technical documentation 
3.	Fulfil requirements on used training, testing and validation data sets 
4.	Achieve appropriate level of accuracy, robustness and cybersecurity
5.	Perform conformity assessment of the system
6.	Register the system to the EU’s database that is accessible to the public
7.	Keep record when the system is in use
8.	Maintain post-market monitoring and report serious incidents and malfunctioning

Suggested tools:
LinkedIn Fairness Toolkit (LiFT) Open source toolkit to enable measurement of fairness according to a multitude of fairness definitions in large-scale machine learning workflows. 

AI Trust Standard & Label The AI Trust Standard & Label describes the characteristics of an AI product with regards to: Transparency, Accountability, Privacy, Fairness and Reliability.

Microsoft Datasheets for Datasets Tool for documenting the datasets used for training and evaluating machine learning models to increase dataset transparency and facilitate better communication between dataset creators and dataset consumers, and encourage the machine learning community to prioritize transparency and accountability.

    """
}
