import openai  # type: ignore # Install with `pip install openai`
import pyttsx3  # type: ignore # Install with `pip install pyttsx3`
import speech_recognition as sr  # type: ignore # Install with `pip install SpeechRecognition`
import datetime

# Initialize OpenAI API Key
openai.api_key = 'your_openai_api_key'  # Replace with your OpenAI API key

class MeetingPodAI:
    def __init__(self):
        self.topics = []
        self.notes = []
        self.engine = pyttsx3.init()  # Initialize text-to-speech engine
        self.recognizer = sr.Recognizer()  # Initialize speech recognizer
        self.mic = sr.Microphone()  # Use the default microphone

    def speak(self, text):
        """Converts text to speech."""
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        """Listens to a response from the user and converts speech to text."""
        with self.mic as source:
            print("Bot: Listening...")
            audio = self.recognizer.listen(source)
            try:
                print("Bot: Recognizing...")
                return self.recognizer.recognize_google(audio)
            except sr.UnknownValueError:
                self.speak("Sorry, I couldn't understand that. Could you repeat?")
                return None
            except sr.RequestError:
                self.speak("Sorry, the speech recognition service is unavailable.")
                return None

    def collect_prompts(self):
        """Collect meeting prompts from the user."""
        self.speak("Welcome to MeetingPod AI! Please provide key topics or prompts you'd like to discuss in the meeting.")
        print("Provide key topics or prompts you'd like to discuss in the meeting. Type 'done' when finished.")
        while True:
            topic = input("Enter a topic or prompt: ")
            if topic.lower() == 'done':
                break
            self.topics.append(topic)
        if not self.topics:
            print("No topics entered. Exiting.")
            self.speak("No topics were entered. Exiting.")
            return False
        return True

    def generate_questions(self, topic):
        """Generate thought-provoking questions using OpenAI GPT."""
        prompt = f"Generate three engaging and thought-provoking questions about the topic: {topic}"
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=150
            )
            questions = response.choices[0].text.strip().split("\n")
            return [q.strip() for q in questions if q.strip()]
        except Exception as e:
            print(f"Error generating questions: {e}")
            self.speak("Sorry, I encountered an error while generating questions.")
            return []

    def get_answer(self, question):
        """Get an answer to a question using OpenAI GPT."""
        prompt = f"Answer the following question as if you were a meeting assistant: {question}"
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=150
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"Error getting answer: {e}")
            self.speak("Sorry, I couldn't generate an answer to that question.")
            return "Sorry, I couldn't provide an answer to that question right now."

    def host_meeting(self):
        """Simulate hosting the meeting and interact with the user."""
        self.speak("Starting the meeting now...")
        print("\nStarting the Meeting...")
        self.speak("Hello everyone! Let's discuss the topics provided.")
        for topic in self.topics:
            self.speak(f"Next topic is {topic}.")
            print(f"\nBot: Next topic is '{topic}'.")
            questions = self.generate_questions(topic)
            if questions:
                for idx, question in enumerate(questions, 1):
                    self.speak(f"Question {idx}: {question}")
                    print(f"Bot: Question {idx}: {question}")
                    response = self.listen()
                    if response:
                        self.notes.append(f"Topic: {topic}\nQ{idx}: {question}\nResponse: {response}\n")
                    else:
                        self.notes.append(f"Topic: {topic}\nQ{idx}: {question}\nResponse: No response recorded.\n")

            # Listen for any extra questions during the meeting
            self.speak("Feel free to ask any questions during the meeting.")
            print("\nBot: Feel free to ask any questions during the meeting.")
            while True:
                participant_question = self.listen()
                if participant_question:
                    if participant_question.lower() == "exit":
                        break
                    answer = self.get_answer(participant_question)
                    self.speak(f"Answer: {answer}")
                    self.notes.append(f"Q: {participant_question}\nA: {answer}\n")
                else:
                    self.speak("I couldn't hear your question. Could you please repeat?")

    def summarize_meeting(self):
        """Generate and save the meeting summary."""
        summary = "\nMeeting Summary\n" + "=" * 30 + "\n"
        for note in self.notes:
            summary += note + "\n"
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"Meeting_Summary_{timestamp}.txt"
        with open(filename, "w") as file:
            file.write(summary)
        self.speak(f"\nMeeting completed! Notes saved as {filename}.")
        print(f"\nMeeting completed! Notes saved as '{filename}'.")
        print("\nThank you for using MeetingPod AI!")

# Main Program
if __name__ == "__main__":
    meeting_pod = MeetingPodAI()
    if meeting_pod.collect_prompts():
        meeting_pod.host_meeting()
        meeting_pod.summarize_meeting()
