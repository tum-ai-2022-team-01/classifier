low_risk_generic_answer = """
The described AI use case is likely to be classified as low-risk according to the EU AI Act. However, please seek further legal advice.

<h5>The list of aspects that make a system high-risk</h5>

<ol>
<li>Biometric identification & categorisation of natural persons</li>
<li>Management and operation of critical infrastructure</li>
<li>Education and vocational training</li>
<li>Employment, workers management and access to self-
employment</li>
<li>Access to and enjoyment of essential private services
and public services and benefits</li>
<li>Law enforcement</li>
<li>Migration, asylum and border control management</li>
<li>Administration of justice and democratic processes</li>
<li>AI as a safety component of regulated products such as but not limited to: Machinery Watercraft, Equipment for explosive atmospheres, Radio equipment, In vitro diagnostic medical devices, Cableway installations, Toys, Lifts, Personal protection equipment, Pressure equipment, Appliances burning fuels, Medical devices</li></ol>
"""

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

    <h5>Required internal assessment check-list for high-risk AI systems</h5>
    <ol>
        <li>Establish a risk management system</li>
        <li>Write up-to-date technical documentation </li>
        <li>Fulfil requirements on used training, testing and validation data sets </li>
        <li>Achieve appropriate level of accuracy, robustness and cybersecurity</li>
        <li>Perform conformity assessment of the system</li>
        <li>Register the system to the EU’s database that is accessible to the public</li>
        <li>Keep record when the system is in use</li>
        <li>Maintain post-market monitoring and report serious incidents and malfunctioning</li>
    </ol>

    <h5>Suggested Tools</h5>

    <ul>
    <li><a href="https://www.microsoft.com/en-us/research/publication/fairlearn-a-toolkit-for-assessing-and-improving-fairness-in-ai/">Microsoft Fairlearn</a> Open source toolkit that empowers data scientists and developers to assess and improve the fairness of their AI systems. Fairlearn has two components: an interactive visualization dashboard and unfairness mitigation algorithms.</li>

    <li><a href="https://cyberwatching.eu/projects/1004/virt-eu/products/virt-eu-service-package">VIRT-EU Service</a> Package Capacity-building material and practical resources to help develop ethically-informed AI systems, based on three different ethical frameworks: virtue ethics, care ethics and capabilities approach.</li>

    <li><a href="https://ai.googleblog.com/2018/09/the-what-if-tool-code-free-probing-of.html">Google What-if Tool</a> What-If Tool let users analyze an ML model without writing code. The What-If Tool has a large set of features, including visualizing your dataset automatically using Facets, the ability to manually edit examples from your dataset and see the effect of those changes, and automatic generation of partial dependence plots which show how the model’s predictions change as any single feature is changed.</li>
    </ul>
    """,
    2: """
    The use case seems to involve the “management and operation of critical infrastructure” including road traffic, water, heat, gas, electricity. These systems have the capacity put people’s life and health at risk.

    <h5>Required internal assessment check-list for high-risk AI systems</h5>
    <ol>
        <li>Establish a risk management system</li>
        <li>Write up-to-date technical documentation </li>
        <li>Fulfil requirements on used training, testing and validation data sets </li>
        <li>Achieve appropriate level of accuracy, robustness and cybersecurity</li>
        <li>Perform conformity assessment of the system</li>
        <li>Register the system to the EU’s database that is accessible to the public</li>
        <li>Keep record when the system is in use</li>
        <li>Maintain post-market monitoring and report serious incidents and malfunctioning</li>
    </ol>

    <h5>Suggested Tools</h5>

   <ul>
    <li><a href="https://www.microsoft.com/en-us/research/publication/fairlearn-a-toolkit-for-assessing-and-improving-fairness-in-ai/">Microsoft Fairlearn</a> Open source toolkit that empowers data scientists and developers to assess and improve the fairness of their AI systems. Fairlearn has two components: an interactive visualization dashboard and unfairness mitigation algorithms.</li>

    <li><a href="https://pp.oecd.ai/en/tmp-tools/tools/ai-trust-standard-label">AI Trust Standard & Label</a> The AI Trust Standard & Label describes the characteristics of an AI product with regards to: Transparency, Accountability, Privacy, Fairness and Reliability.</li>

    <li><a href="https://huggingface.co/spaces/autoevaluate/model-evaluator?dataset=acronym_identification">Evaluate Library and Evaluation on the Hub (Hugging Face)</a> The Evaluation on the Hub platform extends the Evaluate library to a free service model: anyone can evaluate any model on any dataset using any compatible metric, without requiring any code. </li>
    </ul>
    """,
    3: """
    The use case seems to involve the applications in educational and vocational settings where the AI system could determine access to education or professional training. There is a risk that these products could produce biased results and could negatively influence the livelihoods of people.

<h5>Required internal assessment check-list for high-risk AI systems</h5>
<ol>
        <li>Establish a risk management system</li>
        <li>Write up-to-date technical documentation </li>
        <li>Fulfil requirements on used training, testing and validation data sets </li>
        <li>Achieve appropriate level of accuracy, robustness and cybersecurity</li>
        <li>Perform conformity assessment of the system</li>
        <li>Register the system to the EU’s database that is accessible to the public</li>
        <li>Keep record when the system is in use</li>
        <li>Maintain post-market monitoring and report serious incidents and malfunctioning</li>
    </ol>

<h5>Suggested Tools</h5>

<ul>
<li><a href="https://github.com/synthesized-io/fairlens">fairlens</a> FairLens is an open source Python library for automatically discovering bias and measuring fairness in data. The package can be used to quickly identify bias, and provides multiple metrics to measure fairness across a range of sensitive and legally protected characteristics such as age, race and sex.</li>

<li><a href="https://interpret.ml/">Microsoft InterpretML</li> Model interpretability helps developers, data scientists and business stakeholders in the organization gain a comprehensive understanding of their machine learning models. It can also be used to debug models, explain predictions and enable auditing to meet compliance with regulatory requirements.</li>

<li><a href="https://pp.oecd.ai/en/tmp-tools/tools/ai-trust-standard-label">AI Trust Standard & Label</a> The AI Trust Standard & Label describes the characteristics of an AI product with regards to: Transparency, Accountability, Privacy, Fairness and Reliability.</li>
</ul>

    """,
    4: """
    The use case seems to be related to “employment, workers management and access to self-employment”. There is a risk that these products could produce biased results and could negatively influence the livelihoods of people.

<h5>Required internal assessment check-list for high-risk AI systems</h5>
<ol>
        <li>Establish a risk management system</li>
        <li>Write up-to-date technical documentation </li>
        <li>Fulfil requirements on used training, testing and validation data sets </li>
        <li>Achieve appropriate level of accuracy, robustness and cybersecurity</li>
        <li>Perform conformity assessment of the system</li>
        <li>Register the system to the EU’s database that is accessible to the public</li>
        <li>Keep record when the system is in use</li>
        <li>Maintain post-market monitoring and report serious incidents and malfunctioning</li>
    </ol>

<h5>Suggested Tools</h5>

<ul>
<li><a href="https://engineering.linkedin.com/blog/2021/using-the-linkedin-fairness-toolkit-large-scale-ai">LinkedIn Fairness Toolkit (LiFT)</a> Open source toolkit to enable measurement of fairness according to a multitude of fairness definitions in large-scale machine learning workflows.</li>

<li><a href="https://www.microsoft.com/en-us/research/project/datasheets-for-datasets/">Microsoft Datasheets for Datasets</a> Tool for documenting the datasets used for training and evaluating machine learning models to increase dataset transparency and facilitate better communication between dataset creators and dataset consumers, and encourage the machine learning community to prioritize transparency and accountability.</li>

<li><a href="https://huggingface.co/spaces/autoevaluate/model-evaluator?dataset=acronym_identification">Evaluate Library and Evaluation on the Hub (Hugging Face)</a> The Evaluation on the Hub platform extends the Evaluate library to a free service model: anyone can evaluate any model on any dataset using any compatible metric, without requiring any code.</li>
</ul>
    """,
    5: """
    The use case seems to be related to essential private and public services, including access to financial services such as credit scoring systems. There is a risk that these products could produce biased results and could negatively influence the livelihoods of people. These use cases can also affect children by determining access to education or evaluating students.


<h5>Required internal assessment check-list for high-risk AI systems</h5>
<ol>
        <li>Establish a risk management system</li>
        <li>Write up-to-date technical documentation </li>
        <li>Fulfil requirements on used training, testing and validation data sets </li>
        <li>Achieve appropriate level of accuracy, robustness and cybersecurity</li>
        <li>Perform conformity assessment of the system</li>
        <li>Register the system to the EU’s database that is accessible to the public</li>
        <li>Keep record when the system is in use</li>
        <li>Maintain post-market monitoring and report serious incidents and malfunctioning</li>
    </ol>

<h5>Suggested Tools</h5>
<ul>
<li><a href="https://interpret.ml/">Microsoft InterpretML</a> Model interpretability helps developers, data scientists and business stakeholders in the organization gain a comprehensive understanding of their machine learning models. It can also be used to debug models, explain predictions and enable auditing to meet compliance with regulatory requirements.</li>

<li><a href="https://cyberwatching.eu/projects/1004/virt-eu/products/virt-eu-service-package">VIRT-EU Service</a> Package Capacity-building material and practical resources to help develop ethically-informed AI systems, based on three different ethical frameworks: virtue ethics, care ethics and capabilities approach.</li>

<li><a href="https://engineering.linkedin.com/blog/2021/using-the-linkedin-fairness-toolkit-large-scale-ai">LinkedIn Fairness Toolkit (LiFT)</a> Open source toolkit to enable measurement of fairness according to a multitude of fairness definitions in large-scale machine learning workflows</li>
</ul>
    """,
    6: """
    The use case seems to be used in law enforcement. There is a risk that these products could produce biased results and could negatively influence the livelihoods of people and cause serious legal issues.


<h5>Required internal assessment check-list for high-risk AI systems</h5>
<ol>
        <li>Establish a risk management system</li>
        <li>Write up-to-date technical documentation </li>
        <li>Fulfil requirements on used training, testing and validation data sets </li>
        <li>Achieve appropriate level of accuracy, robustness and cybersecurity</li>
        <li>Perform conformity assessment of the system</li>
        <li>Register the system to the EU’s database that is accessible to the public</li>
        <li>Keep record when the system is in use</li>
        <li>Maintain post-market monitoring and report serious incidents and malfunctioning</li>
    </ol>

<h5>Suggested Tools</a>
<ul>
<li><a href="https://huggingface.co/docs/hub/model-cards">Model Cards (Hugging Face)</a> Model cards are short documents accompanying trained machine learning (ML) models that provide benchmarked evaluation in a variety of conditions.. Model cards also disclose the context in which models are intended to be used, details of the performance evaluation procedures, and other relevant information. This framework can be used to document any trained ML model.</li>

<li><a href="https://github.com/synthesized-io/fairlens">fairlens</a> FairLens is an open source Python library for automatically discovering bias and measuring fairness in data. The package can be used to quickly identify bias, and provides multiple metrics to measure fairness across a range of sensitive and legally protected characteristics such as age, race and sex.</li>

<li><a href="https://interpret.ml/">Microsoft InterpretML</a> Model interpretability helps developers, data scientists and business stakeholders in the organization gain a comprehensive understanding of their machine learning models. It can also be used to debug models, explain predictions and enable auditing to meet compliance with regulatory requirements.</li>
</ul>
    """,
    7: """
    The use case seems to be used in the context of “migration, asylum and border control management” There is a risk of these system producing biased and discriminatory results based on physical characteristics.

<h5>Required internal assessment check-list for high-risk AI systems</h5>
<ol>
        <li>Establish a risk management system</li>
        <li>Write up-to-date technical documentation </li>
        <li>Fulfil requirements on used training, testing and validation data sets </li>
        <li>Achieve appropriate level of accuracy, robustness and cybersecurity</li>
        <li>Perform conformity assessment of the system</li>
        <li>Register the system to the EU’s database that is accessible to the public</li>
        <li>Keep record when the system is in use</li>
        <li>Maintain post-market monitoring and report serious incidents and malfunctioning</li>
    </ol>

<h5>Suggested Tools</h5>
<ul>
<li><a href="https://www.microsoft.com/en-us/research/project/datasheets-for-datasets/">Microsoft Datasheets for Datasets</a> Tool for documenting the datasets used for training and evaluating machine learning models to increase dataset transparency and facilitate better communication between dataset creators and dataset consumers, and encourage the machine learning community to prioritize transparency and accountability.</li>

<li><a href="https://github.com/synthesized-io/fairlens">fairlens</a> FairLens is an open source Python library for automatically discovering bias and measuring fairness in data. The package can be used to quickly identify bias, and provides multiple metrics to measure fairness across a range of sensitive and legally protected characteristics such as age, race and sex.</li>

<li><a href="https://engineering.linkedin.com/blog/2021/using-the-linkedin-fairness-toolkit-large-scale-ai">LinkedIn Fairness Toolkit (LiFT)</a> Open source toolkit to enable measurement of fairness according to a multitude of fairness definitions in large-scale machine learning workflows.</li>
</ul>
    """,
    8: """
    The use case seems to be used for “administration of justice and democratic processes”. Assist in judicial systems such as using AI to research facts and the law carries the risk of producing false legal assumptions during judicial processes and requires constant human supervision.


<h5>Required internal assessment check-list for high-risk AI systems</h5>
<ol>
        <li>Establish a risk management system</li>
        <li>Write up-to-date technical documentation </li>
        <li>Fulfil requirements on used training, testing and validation data sets </li>
        <li>Achieve appropriate level of accuracy, robustness and cybersecurity</li>
        <li>Perform conformity assessment of the system</li>
        <li>Register the system to the EU’s database that is accessible to the public</li>
        <li>Keep record when the system is in use</li>
        <li>Maintain post-market monitoring and report serious incidents and malfunctioning</li>
    </ol>

<h5>Suggested Tools</h5>
<ul>
<li><a href="https://engineering.linkedin.com/blog/2021/using-the-linkedin-fairness-toolkit-large-scale-ai">LinkedIn Fairness Toolkit (LiFT)</a> Open source toolkit to enable measurement of fairness according to a multitude of fairness definitions in large-scale machine learning workflows.</li>

<li><a href="https://pp.oecd.ai/en/tmp-tools/tools/ai-trust-standard-label">AI Trust Standard & Label</a> The AI Trust Standard & Label describes the characteristics of an AI product with regards to: Transparency, Accountability, Privacy, Fairness and Reliability.</li>

<li><a href="https://www.microsoft.com/en-us/research/project/datasheets-for-datasets/">Microsoft Datasheets for Datasets</a> Tool for documenting the datasets used for training and evaluating machine learning models to increase dataset transparency and facilitate better communication between dataset creators and dataset consumers, and encourage the machine learning community to prioritize transparency and accountability.</li>
</ul>
    """
}
