import streamlit as st
import pandas as pd

#Author: Marcus C. Rodriguez 04/03/2024

# Function to simulate creation of a photon with given wavelength
def create_photon(wavelength):
    # Simulate creation of a photon with specified wavelength
    return f"Photon Approximated Wavelength: {wavelength} nm"

# Function to map slider values to RGB color and corresponding wavelength
def map_to_color_and_wavelength(behavior, emotion, decision):
    #Map slider values to RGB color range (0-255)
    if behavior < 1:
    	behavior = ((behavior) +1)/2
    if emotion < 1:
    	emotion = ((emotion) +1)/2
    if decision < 1:
    	decision = ((decision) +1)/2
    	
    r = int(behavior * 255)
    g = int(emotion * 255)
    b = int(decision * 255)
    
    # Calculate corresponding wavelength (rough approximation)
    if ((r + g + b) == 0):
    	wavelength = "N/A"
    else:
    	wavelength = int((r * 625 + g * 525 + b * 470) / (r + g + b))
    return (r, g, b), wavelength

# Main Streamlit app
def main():
    left_co, cent_co, last_co = st.columns(3)
    with cent_co:
    	st.image('mind.png', width = 300, caption = 'Dr. Richard Conner, Dr. Daniel Winterhalter & Marcus C. Rodriguez')
    st.markdown('[www.marcusc.com](https://www.marcusc.com)')
    
    # Define sliders for behavior, emotion, and decision
    st.subheader('Semantic Differentiation of the Mind:', divider='rainbow')
    st.write('A 3 Channel, Quantum Data Architecture *Patent Pending: [Appl. No.17/321,457](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/20220374919)')
    behavior = st.slider("(B)ehavior", -1.0, 1.0, 0.0, step = 0.10)
    emotion = st.slider("(E)motion", -1.0, 1.0, 0.0, step = 0.10)
    decision = st.slider("(D)ecision", -1.0, 1.0, 0.0, step = 0.10)

    # Map slider values to RGB color and corresponding wavelength
    color, wavelength = map_to_color_and_wavelength(behavior, emotion, decision) 
          
    with left_co:
    	st.markdown(
        	f'<div style="width: 100px; height: 100px; background-color: rgb{color};"></div>',
        	unsafe_allow_html=True
    		)
    		
    # Simulate creation of a photon with corresponding wavelength
    with left_co:
    	photon_message = create_photon(wavelength)
    	st.write(photon_message)
    	#st.write(color)
    	
    # Table of Examples of BED Duality
    st.write("Examples of Duality (low state -1/high state +1):")
    df = pd.DataFrame(
    	[
    		{"(B)ehavior": "Don't do it / Do it", "(E)motion": "Sad / Happy", "(D)ecision": "Don't Like / Like"},
    		{"(B)ehavior": "Flee / Fight", "(E)motion": "Afraid / Angry", "(D)ecision": "Threat / Not a Threat"},
    		{"(B)ehavior": "Don't Buy it / Buy it", "(E)motion": "Sad / Happy", "(D)ecision": "Don't Like / Like"},
    		{"(B)ehavior": "Don't Vote for him/her / Vote for him/her", "(E)motion": "Fear / Anger", "(D)ecision": "Bad / Good"},
    		{"(B)ehavior": "Reject / Accept", "(E)motion": "Sad / Happy", "(D)ecision": "Don't Like / Like"},
    	]
    )
    st.dataframe(df, use_container_width=True)
    st.markdown('The idea that human cognition may exhibit quantum mechanical properties or be influenced by quantum phenomena is a topic of ongoing debate and exploration in various scientific disciplines, including neuroscience, psychology, and quantum physics. This concept, often referred to as "quantum cognition" or "quantum mind", suggests that certain aspects of human cognition may not be fully explained by classical (non-quantum) models and could potentially be better understood through the lens of quantum mechanics.')
    st.divider() 
    st.markdown(':red[**Skeptical View**:] Some scientists are skeptical of the notion that human cognition is inherently quantum mechanical, arguing that classical models adequately explain most cognitive phenomena. They point out that quantum effects are typically observed at very small scales, such as in individual atoms or molecules, whereas cognitive processes occur at larger scales involving billions of neurons and synapses. In the 1990’s Penrose and Hameroff proposed the (Orch OR) theory suggesting that consciousness originates at a quantum level inside neurons, which has been widely dismissed for many of the reasons stated above.') 
    st.markdown(':red[**Quantum Cognition Hypothesis**:] Proponents of the quantum cognition hypothesis argue that certain cognitive phenomena, such as decision-making under uncertainty, concept combination, and problem-solving, exhibit patterns that resemble quantum phenomena such as superposition, entanglement, and interference. They propose that quantum models may provide a more accurate description of these phenomena than classical models. It is our contention that thinking is a quantum phenomena. ') 
    st.markdown(':red[**Interdisciplinary Research**:] Interdisciplinary research at the intersection of quantum physics and cognitive science aims to explore potential connections between quantum mechanics and human cognition. This research involves theoretical modeling, empirical studies, and computational simulations to investigate whether and how quantum principles may manifest in cognitive processes.')
    st.markdown(':red[**Emerging Evidence**:] While the evidence for quantum effects in human cognition is still preliminary, some studies have reported intriguing findings that suggest quantum-like phenomena may play a role in certain cognitive tasks. For example, research on decision-making and concept representation has shown patterns of behavior consistent with quantum models.')
    st.divider()
    st.markdown(':red[**Semantic Differentiation and Quantum Mechanics**] at first glance may seem unrelated, but there are intriguing parallels between the two. Transformer architectures that underpin Large Language Models (LLMs) operate in a vector space where the relationships between words are represented in a high-dimensional semantic space. This vector space representation has some conceptual connections to principles from quantum mechanics, such as superposition and entanglement.')
    st.markdown(':red[**High-Dimensional Space**:] In both quantum mechanics and vector space representations, entities (particles, words or in our case states of mind) are represented as vectors in a high-dimensional space. This space allows for complex relationships and interactions between entities to be captured.')
    st.markdown(':red[**Complexity and Non-linearity**:] Both fields deal with complex systems that exhibit non-linear behavior. In quantum mechanics, the behavior of particles at the subatomic level is often non-intuitive and non-linear. Similarly, in semantic differentiation, the meaning of words or concepts can be highly nuanced and influenced by context, leading to complex interactions.')
    st.markdown(':red[**Superposition**:] Just as quantum particles can exist in multiple states simultaneously (superposition), words as well as state of mind vectors can represent multiple meanings or contexts simultaneously. For example, the word "bank" can represent both a financial institution and the side of a river, depending on the context. In the same manner a behavior in one context could be deemed normal, while in another it could be deviant. The interpretation is a reflection of the image bisecting the wave of consciousness at that point which is both real and imaginary and a direct reflection of the identity of the observer. In our simulation, the state of the photon is not limited to a single wavelength but can exist in a combination of multiple wavelengths simultaneously in the participant’s mind. The state is resolved upon the participant moving the sliders, crossing the threshold of the imaginary to the real.')
    st.markdown(":red[**Entanglement and Interconnectedness**:] In quantum mechanics, entanglement refers to the phenomenon where the properties of two or more particles are correlated, even when they are spatially separated. Quantum entanglement describes a phenomenon where particles become correlated with each other in such a way that the state of one particle is dependent on the state of another, even when they are separated by large distances. In a similar vein, semantic differentiation acknowledges the interconnectedness of concepts and words, where the meaning of one word can influence the interpretation of another. An image or other person may also influence another person’s state of mind and interpretations. Similarly, in vector space models, word vectors can be entangled in the sense that the meaning of one word may be influenced by the context of another word in a sentence or document across space and time. In much the same way a state of mind vector can be entangled between two observers of an image across space and time. The state of the photon becomes correlated with the mental state of the user or with other quantum systems. Mechanisms may be implemented to simulate entanglement between the photon and the user's mental state, allowing for non-local correlations and interactions.")
    st.markdown(':red[**Uncertainty and Probability**:] Quantum mechanics is founded on the principle of uncertainty, where the behavior of particles is described by probability distributions rather than deterministic outcomes. Similarly, semantic differentiation acknowledges the uncertainty in human language and meaning, recognizing that words can have multiple interpretations and shades of meaning. Both quantum mechanics and vector space models operate with probabilistic relationships. In quantum mechanics, the state of a system is described by a wave function, which gives the probability amplitude of finding the system in a particular state. Similarly, in vector space models, the similarity between words or the likelihood of a word or a state of mind occurring in a context is represented by probabilistic measures.')
    st.markdown("While the analogy between vector space models and quantum mechanics is intriguing, it's important to note that they operate in fundamentally different domains. Vector space models are primarily used in natural language processing, machine learning and in our case to model and influence human emotional and behavioral states (state of mind), where they serve as powerful tools for representing and analyzing complex data sets. On the other hand, quantum mechanics describes the behavior of particles at the quantum scale and has applications in various fields, including physics, chemistry, and computation. Nonetheless, exploring the connections between these domains can lead to interesting insights and potential cross-disciplinary applications. As research in quantum computing, natural language processing and quantum information science continues to advance, we may see further convergence and collaboration between these fields especially in the advancement of AGI.")
    st.divider()
    st.markdown(":red[**The Project**] In this basic simulation, we use  sliders that correlate to a human’s state of mind (BED vectors moving) at a given time to illustrate theoretically generating a corresponding, nearly coherent photon, analogous to a qubit in quantum computing with a slow light laser. Simulating the creation of a photon with a wavelength corresponding to the color displayed on the screen is indeed a quantum mechanical process. In the context of the code provided, the manipulation of the properties of the simulated photon to match the wavelength of the displayed color is analogous to a quantum manipulation, even though it's a simplified simulation. By adjusting the sliders representing behavior, emotion, and decision (state of mind), users effectively influence the color (wavelength) of the photons emitted by the monitor, which in turn could be interpreted as a manipulation of the properties of a simulated photon. While the code provided is simplified for demonstration purposes and does not encompass the full complexity of quantum mechanics, it illustrates how user input and mental state may be intertwined quantum phenomena. In a more advanced implementation, additional quantum mechanical principles and calculations could be integrated to provide a more accurate simulation of photon creation and manipulation using a slow slight laser. In a more advanced implementation aimed at the creation and manipulation of photons in a quantum-mechanical context based on user input and mental states, several enhancements could be made:")
    st.markdown(":red[**Slider Manipulation**:] The sliders representing behavior, emotion, and decision are used to manipulate the state of the nearly coherent photon. Each slider corresponds to a specific parameter of the photon's state, such as its frequency, polarization, or phase.")
    st.markdown(":red[**Slow Light Laser**:] A slow light laser could be employed to create the nearly coherent photon. Slow light lasers are capable of producing photons with precise characteristics and can be controlled to interact with external stimuli.")
    st.markdown(":red[**Quantum Gates and Manipulation**:] Various quantum gates, analogous to those used in quantum computing, could be applied to the photon's state to manipulate its properties. These gates could correspond to different operations on the photon, such as phase shifts, polarization rotations, or frequency conversions. The gates could also be directly applied to the human brain such as video, ar/vr or another person talking and the impact measured by the corresponding generated photons.")
    st.markdown(":red[**State Transfer**:] The state of the photon, influenced by the settings of the sliders and manipulated by quantum gates, could be transferred from the imaginary realm of the mind to physical space using the slow light laser. This transfer could occur at a predefined time, t, synchronized with the user's input or according to a predetermined schedule.")
    st.markdown(":red[**Observer Interaction**:] The resulting state of the photon, after manipulation by the quantum gates and transfer via the slow light laser, could manifest as observable changes in the photon's properties, such as its color, intensity, or direction. These changes could be perceived by an observer, providing feedback on the user's mental state and the effects of external stimuli measured by the slider settings.")
    st.markdown(":red[**Recording and Analysis**:] The state of the photon, as influenced by the user's mental state and corresponding slider settings, could be recorded and analyzed for further insights. Data analysis techniques could be employed to extract patterns or correlations between the slider settings, photon properties, and the user's mental state, specifically AI including Deep Neural Networks, Reinforcment Learning algorithms (PPO) that would be more robust based on the unique quantum data architecture used for training.")
    st.markdown(":red[**Feedback Loop**:] A feedback loop could be established to continuously adjust the slider settings based on the observed effects on the photon's state and the user's mental state. This iterative process could help refine the mapping between the user's subjective experience and the properties of the photon, improving the accuracy and effectiveness of the system over time.")
    st.markdown("By integrating these components, a novel system may be created that allows users to interactively manipulate the state of a nearly coherent photon using sliders representing their state of mind. This concept combines elements of quantum optics, quantum computing, and human-computer interaction to create a unique interface for exploring the relationship between consciousness and quantum phenomena. How else can we collect data?")
    st.divider()
    st.markdown(":red[**EEG (Electroencephalography) and/or Brain Computer Interfaces (BCI)**] will replace the sliders, allowing for a more direct and dynamic interaction between the user's brainwaves and the state of the photon.") 
    st.markdown(":red[**EEG or BCI Data Acquisition**:] EEG sensors may be placed on the user's scalp to measure electrical activity in the brain. These sensors detect brain waves associated with different mental states, such as attention, relaxation, cognitive workload and may also detect emotions.")
    st.markdown(":red[**Brainwave Analysis**:] The EEG signals captured by the sensors would be processed and analyzed in real-time to extract meaningful features corresponding to the user's mental state. Signal processing algorithms could be used to identify patterns or signatures indicative of specific cognitive states related to behavior, emotions and thoughts or decisions.")
    st.markdown(":red[**Mapping to Photon State**:] The extracted features from the EEG signals would be mapped to parameters of the nearly coherent photon's state. For example, certain brainwave patterns could be associated with changes in the photon's frequency, polarization, or phase. This mapping would establish a direct link between the user's mental state and the properties of the photon.")
    st.markdown(":red[**Photon Manipulation**:] Quantum gates and control mechanisms would be employed to manipulate the state of the photon based on the mapped EEG features. These gates could be controlled in real-time to adjust the photon's properties according to the user's changing mental state.")
    st.markdown(":red[**Photon Emission and Observation**:] The manipulated photon would be emitted by the slow light laser and observed by the user or an external observer. Changes in the photon's properties, such as its color, intensity, or direction, would provide real-time feedback on the user's mental state as modulated by the EEG signals.")
    st.markdown(":red[**Closed-loop Feedback**:] A closed-loop feedback system could be established to continuously monitor the user's brainwaves, adjust the manipulation of the photon accordingly, and provide feedback to the user based on the observed effects. This feedback loop would enable dynamic interaction and adaptation based on the user's ongoing cognitive state.")
    st.markdown("By integrating EEG or other similar brain imaging technology into the system, you create a more immersive and responsive interface that directly reflects the user's cognitive processes in real-time. This approach would offer a novel means of exploring the relationship between brain activity and quantum phenomena, opening up new possibilities for interactive experiences and cognitive augmentation. By incorporating EEG technology into the system, you could capture and measure the subject's emotional and cognitive states in real-time while they are watching a video or engaging with any other stimuli. The EEG signals provide direct insights into the subject's mental processes, allowing for a more nuanced and dynamic interaction with the photon or any other output medium. For example, while the subject watches a video, the EEG sensors would continuously monitor their brainwaves. The detected brainwave patterns could then be analyzed to infer the subject's emotional responses, cognitive engagement, attention levels, and other mental states. This information could be mapped to parameters of the photon's state, such as its color, intensity, or frequency, to create a real-time visualization of the subject's inner experiences. Overall, integrating EEG technology into multimedia experiences opens up exciting possibilities for creating more immersive, personalized, and engaging interactions that bridge the gap between technology and human cognition.")
    st.divider()
    st.markdown(":red[**What to do with the data/models?**] Applying the Law of Large Numbers (LLN) to explore human behavior, emotions, and decisions in aggregate, and drawing from the principles of quantum mechanics (QM) creates an unprecedented opportunity as technology evolves:")
    st.markdown(":red[**Law of Large Numbers (LLN)**:] The LLN states that as the number of observations or trials increases, the average of the observed values converges to the expected value. In the context of human behavior, emotions, and decisions, this principle suggests that by observing large populations or groups of individuals, patterns and regularities may emerge that allow us to make predictions about collective behavior.")
    st.markdown(":red[**Analogous Predictive Framework**:] By drawing an analogy between the collective behavior of large populations of humans and the behavior of subatomic particles governed by quantum mechanics, we can conceive of a predictive framework where statistical regularities observed at the macroscopic level are analogous to quantum phenomena observed at the microscopic level.")
    st.markdown(":red[**Quantum-Inspired Models**:] Researchers have already begun exploring quantum-inspired models for understanding complex systems beyond the realm of quantum physics, including social networks, financial markets, and biological systems. These models leverage principles from quantum mechanics, such as superposition and entanglement, to describe emergent properties and dynamics in large-scale systems.")
    st.markdown(":red[**Emergent Phenomena**:] Just as quantum phenomena emerge from the collective behavior of subatomic particles, emergent phenomena in complex systems may arise from the interactions and dynamics of large populations of individuals. By applying insights from quantum-inspired models, we may gain a deeper understanding of how collective behavior emerges from individual interactions and influences.")
    st.markdown(":red[**Predictive Power**:] By leveraging the predictive power of quantum-inspired models and the statistical regularities observed in large populations, we may be able to make more accurate predictions about societal trends, market dynamics, and other complex phenomena that defy simple deterministic explanations.")
    st.markdown("Overall, while the application of quantum mechanics to predict human behavior and societal dynamics is still in its early stages, the idea of using principles from quantum physics to explore emergent properties and patterns in complex systems holds promise for advancing our understanding of collective behavior and decision-making. Continued interdisciplinary research at the intersection of quantum physics, complex systems theory, and social science may lead to novel insights and predictive models with broad applications.")
    st.divider()
    st.markdown(":red[**Schrödinger's Equation**] is a fundamental equation in quantum mechanics, describing how the quantum state of a physical system changes over time. It's typically written as a partial differential equation involving the wave function of the system. In the context of Schrödinger's equation, the real part of the wave function represents the observable properties of the system, such as position or momentum, while the imaginary part represents the phase or probability amplitude. The absolute square of the wave function -i.e., the magnitude of the complex-valued wave function- squared gives the probability density of finding the system in a particular state. How is Schrödinger's equation related to the sliders being moved and recorded as real and imaginary components:")
    st.markdown(":red[**Real Component (Observable Properties)**:]  In Schrödinger's equation, the real component of the wave function represents observable properties of the system, such as position or momentum. Similarly, in the context of the sliders, the real component could represent observable aspects of the individual's state of mind, behavior, or emotions. For example, the position of the sliders corresponds to specific behavioral traits or emotional states that are directly observable or measurable such as images from a camera -non-verbal communication.")
    st.markdown(":red[**Imaginary Component, Probability Amplitude**:] In Schrödinger's equation, the imaginary component of the wave function represents the phase or probability amplitude of the system. Analogously, in the context of the sliders, the imaginary component could represent the underlying probabilistic aspects of the individual's state of mind. This might include latent or unobservable factors that influence behavior or emotions but are not directly measurable. For example, it could represent subconscious influences, biases, or predispositions that shape decision-making processes.")
    st.markdown(":red[**Recording and Analysis**:] By recording both the real and imaginary components of the sliders' positions over time, we can capture both the observable and probabilistic aspects of the individual's state of mind. Analyzing these recorded components allows us to gain insights into the dynamics of the individual's behavior, emotions, and decision-making processes. We can identify patterns, correlations, and dependencies between the observable and probabilistic components, shedding light on the underlying mechanisms driving human cognition.")
    st.markdown(":red[**Recording the Real Values (BED)**:] The real component represents the observable aspects of the individual's state of mind, including their behavior, emotions, and decisions (BED). At each time t,  the individual's current state of BED is recorded, providing a snapshot of their observable characteristics at that moment. These recorded values serve as the basis for analyzing and understanding the individual's overt actions, feelings, and cognitive processes.")
    st.markdown(":red[**Capturing the Imaginary Component, Differential**:] The imaginary component, which represents the probabilistic aspects or underlying dynamics of the individual's state of mind, is captured as the differential between two recorded values in time t. By computing the difference or change between consecutive recorded values of BED, we can infer how the individual's state of mind is evolving over time. This differential captures the rate of change or flux in the individual's behavior, emotions, or decisions, providing insights into the dynamics of their cognitive processes beyond what is directly observable.")
    st.markdown(":red[**Interpreting the Imaginary Component**:] The imaginary component, derived from the differentials between recorded BED values, encapsulates latent or hidden aspects of the individual's cognition that may not be directly observable. It may represent shifts in underlying motivations, cognitive biases, or subconscious influences that affect the individual's observable behavior and emotional states. Analyzing the temporal patterns and trends in the imaginary component allows us to uncover subtle changes or trends in the individual's state of mind, offering deeper insights into their cognitive processes, decision-making mechanisms and identity.")
    st.markdown(":red[**Integrating the Imaginary with Real Component**:] By integrating the real and imaginary components, we can construct a comprehensive model of the individual's cognitive dynamics, incorporating both observable behaviors and underlying probabilistic influences. This integrated approach allows us to capture the multidimensional nature of human cognition, recognizing the interplay between overt actions and latent cognitive processes. By considering both components, we can develop richer insights into the complexities of human behavior, emotions, and decision-making, facilitating more nuanced understanding and prediction of individual responses and outcomes.")
    st.markdown("In summary, by recording the real values of BED at each time t  and capturing the imaginary component as the differential between consecutive recorded values, we can construct a holistic framework for analyzing and understanding the dynamics of human cognition. This approach enables us to explore the interplay between observable behaviors and underlying probabilistic influences, leading to deeper insights into the complexities of human consciousness,  decision-making processes and identity. Overall, the question of whether human cognition is a quantum phenomenon remains open and subject to further investigation. While there are intriguing parallels between quantum mechanics and certain cognitive phenomena, more empirical research and theoretical development are needed to fully understand the nature and extent of any potential connections. Regardless of the outcome, exploring the possibility of quantum cognition can lead to new insights into the nature of consciousness, perception and identity. marcuscrodriguez@outlook.com")
    st.divider() 

if __name__ == "__main__":
    main()
    
    