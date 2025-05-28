# Web Scraping Agent Use Cases

## Good examples

**Use Case 1:**
*   **Prompt:** "Give me bulletpoints about what this page is about: https://www.constellation-guide.com/constellation-list/corvus-constellation/"
*   **Desired Outcome:** A bulletpoint list about the contents of the page, made easily digestible.
*   **Actual response example:**
```
Here are some bullet points about the Corvus constellation:

- **Name**: Corvus (the Crow)
- **Location**: Southern sky, third quadrant (SQ3)
- **Size**: 184 square degrees, 70th in size
- **Neighboring Constellations**: Crater, Hydra, Virgo
- **Brightest Star**: Gienah (Gamma Corvi, magnitude 2.59)
- **Notable Features**:
  - Home to the famous Antennae Galaxies (NGC 4038/NGC 4039)
  - Contains the planetary nebula NGC 4361
  - The Sail or Spica's Spanker asterism points to Spica (Alpha Virginis)
- **Mythology**: Represents Apollo's sacred bird, the raven, in Greek mythology
- **Visibility**: Can be seen from latitudes between +60° and -90°
```

**Use Case 2:**
*   **Prompt:** "What was new at google io 2025? https://blog.google/technology/developers/google-io-2025-collection/"
*   **Desired Outcome:** A list of all the things that were announced at this years Google I/O 2025.
*   **Actual response example:**
```
Here are the main headlines from the Google I/O 2025 conference:

1. **Gemini 2.5: Our Most Intelligent Models Get Even Better**
   - Updates to the Gemini 2.5 model series and Deep Think, an experimental enhanced reasoning mode for 2.5 Pro.

2. **AI Mode Comes to Search for Everyone in the U.S.**
   - AI Mode is now rolling out to everyone in the U.S.

3. **Gemini App Gets More Personal, Proactive, and Powerful**
   - Updates include Veo 3, Imagen 4, Deep Research, and Canvas.

4. **Flow: AI-Powered Filmmaking with Veo 3**
   - A new AI filmmaking tool built with and for creatives.

5. **Google AI Ultra: The Best of Google AI in One Subscription**
   - Google's new AI subscription with the highest access to its most capable models and premium features.

6. **Shop with AI Mode and Try Clothes on Yourself Virtually**
   - New shopping features in AI Mode and a virtual try-on tool.

7. **Building with AI: Highlights for Developers at Google I/O**
   - New tools to help developers build AI applications.

8. **Learn in Newer, Deeper Ways with Gemini**
   - Google is infusing LearnLM directly into Gemini 2.5.

9. **Android XR Brings Gemini to Glasses and Headsets**
   - Android XR and Gemini are coming to devices like glasses and headsets.

10. **Google Beam: AI-First 3D Video Communication Platform**
    - Project Starline becomes Google Beam, using AI to turn 2D video streams into realistic, immersive video calls.

11. **SynthID Detector: A New Portal to Help Identify AI-Generated Content**
    - A new portal to help identify AI-generated content.

12. **Coding with Gemini Gets Easier**
    - Gemini Code Assist for individuals and GitHub are now generally available and powered by Gemini 2.5.

13. **Build with Jules, Your Asynchronous Coding Agent**
    - Google's autonomous coding agent Jules is now in public beta.

14. **AI in Filmmaking: Google DeepMind Partners with Darren Aronofsky**
    - Primordial Soup explores AI's role in storytelling.

15. **AI Overviews Now Available in Over 200 Countries and Territories**
    - AI Overviews are launching in new countries and languages.

16. **Gemini Diffusion: Our New Experimental Research Model**
    - Gemini Diffusion is a text diffusion model.

17. **Workspace with Gemini Helps You Do Your Best Work**
    - AI is being brought into Workspace.

18. **Gemma 3n Preview: Powerful, Efficient, Mobile-First AI**
    - The latest Google open model for accessible AI.

19. **Expanding Gemini 2.5 Flash and Pro Capabilities for Enterprises**
    - New capabilities for Gemini 2.5 Flash and 2.5 Pro on Vertex AI.

20. **Expanding Vertex AI with the Next Wave of Generative AI Media Models**
    - New generative AI media models on Vertex AI.

21. **Advancing Gemini’s Security Safeguards**
    - A new white paper outlines security improvements in Gemini 2.5.

22. **What’s New in Firebase at Google I/O 2025**
    - Updates to Firebase to help build the next generation of apps.
```

**Use Case 3:**
*   **Prompt:** "What does the synopsis say? https://myanimelist.net/anime/2236/Toki_wo_Kakeru_Shoujo"
*   **Desired Outcome:** A direct transcription of what the synopsis chapter says of this page about an anime movie.
*   **Actual response example:**
```
The synopsis of Toki wo Kakeru Shoujo (The Girl Who Leapt Through Time) is as follows:

Makoto Konno is in her last year of high school, but is having a hard time deciding what to do with her future. In between enduring the pressure of her teachers and killing time with her best friends, Makoto's life suddenly changes when she accidentally discovers that she is capable of literally leaping through time. Toki wo Kakeru Shoujo follows Makoto as she plays around with her newfound power. However, she soon learns the hard way that every choice has a consequence, and time is a lot more complicated than it may seem.
```

**Use Case 4:**
*   **Prompt:** "From the following webpage: https://www.google.com/finance/quote/META:NASDAQ extract the current stock price of META."
*   **Desired Outcome:** The current stock price of META.
*   **Actual response example:**
```
The current stock price of META (Meta Platforms Inc) is $644.64.
```

**Use Case 5:**
*   **Prompt:** "Summarize this article https://www.npr.org/2025/05/22/nx-s1-5407548/openai-jony-ive-io-deal-ai-devices"
*   **Desired Outcome:** A summarization of an article about OpenAI acquiring io.
*   **Actual response example:**
```
Here is the summary of the article "OpenAI buys io, former Apple designer Jony Ive’s device startup" from NPR:

OpenAI, the creator of ChatGPT, has acquired io, a device startup founded by former Apple designer Jony Ive, in a deal worth $6.5 billion. The acquisition aims to combine OpenAI's AI capabilities with Ive's design expertise to create a new line of AI-enabled devices. The new devices will be designed to let people use AI to create various things, as current devices are not optimized for AI. Ive and his design firm LoveFrom will assume design and creative responsibilities across OpenAI and io. The companies plan to share their work publicly next year.
```

## Failed examples

**Failed example 1:**
*   **Prompt:** "What is on this page? https://www.anthropic.com/news/claude-4"
*   **Desired Outcome:** A description of what is on the page. However this actually returns an error.
*   **Actual response example:**
```
I'm sorry, but it seems like I couldn't access the main content of the page because it returned an error message. The error message was: "Application error: a client-side exception has occurred (see the browser console for more information)."
```

**Failed example 2:**
*   **Prompt:** "Read the first comment: https://www.reddit.com/r/ClaudeAI/comments/1kxep8w/anthropic_ceo_goes_on_record_about_job_losses/"
*   **Desired Outcome:** A direct transcription of what the first comment said. However, the tool call seemed to have failed as it returns: 'You've been blocked by network security. If you think you've been blocked by mistake, file a ticket below and we'll look into it. File a ticket'
*   **Actual response example:**
```
I'm sorry, but it seems like I can't access the content of the Reddit page because I've been blocked by network security."
```

**Failed example 3:**
*   **Prompt:** "Summarize this page https://medium.com/data-science-at-microsoft/how-large-language-models-work-91c362f5b78f"
*   **Desired Outcome:** A summarization of the page provided. However, the page has human verification implemented, and can therefore not read the content.
*   **Actual response example:**
```
I'm sorry, but it seems I can't access the main content of the page because it returned a security verification form.
```