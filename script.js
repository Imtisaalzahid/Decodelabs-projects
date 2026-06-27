// Rule-Based Chatbot Logic with clean control flow & if-else conditions

const chatMessages = document.getElementById('chatMessages');
const userInput = document.getElementById('userInput');
const chatForm = document.getElementById('chatForm');
const sendBtn = document.getElementById('sendBtn');
const clearChatBtn = document.getElementById('clearChatBtn');
const restartBtn = document.getElementById('restartBtn');
const botStatus = document.getElementById('botStatus');

let isSessionActive = true;

// Initial Welcome Message
window.addEventListener('DOMContentLoaded', () => {
    addBotMessage("Hello! I am a Rule-Based AI Chatbot 🤖. Type a message or click one of the suggested prompts to start chatting!");
});

// Event Listeners for action buttons
clearChatBtn.addEventListener('click', () => {
    chatMessages.innerHTML = '';
    if (isSessionActive) {
        addBotMessage("Chat history cleared! How can I help you?");
    }
});

restartBtn.addEventListener('click', () => {
    chatMessages.innerHTML = '';
    isSessionActive = true;
    userInput.disabled = false;
    sendBtn.disabled = false;
    userInput.placeholder = "Type a message (e.g., 'hello', 'how are you', 'bye')...";
    botStatus.textContent = "Online & Ready";
    botStatus.style.color = "#94a3b8";
    addBotMessage("Session restarted! 🔄 Ready for your inputs.");
});

function sendSuggested(text) {
    if (!isSessionActive) return;
    userInput.value = text;
    handleSendMessage(new Event('submit'));
}

function handleSendMessage(e) {
    if (e) e.preventDefault();
    
    const messageText = userInput.value.trim();
    if (!messageText || !isSessionActive) return;

    // Add User Message to Chat Window
    addUserMessage(messageText);
    userInput.value = '';

    // Simulate typing delay for realistic interaction
    setTimeout(() => {
        processRuleBasedResponse(messageText);
    }, 400);
}

/**
 * Core Rule-Based Decision Logic using strict IF-ELSE IF control flow
 * as specified in project requirements.
 */
function processRuleBasedResponse(rawInput) {
    const text = rawInput.toLowerCase().trim();

    let response = "";
    let isExitCommand = false;

    // Rule 1: Greetings Check
    if (text.includes("hello") || text.includes("hi") || text.includes("hey") || text.includes("greetings") || text.includes("good morning") || text.includes("good evening")) {
        response = "Hello there! 👋 Welcome! How can I assist you today?";
    }
    // Rule 2: Exit Commands Check
    else if (text === "bye" || text === "exit" || text === "quit" || text.includes("goodbye") || text.includes("see you")) {
        response = "Goodbye! 👋 It was great chatting with you. Have a fantastic day!";
        isExitCommand = true;
    }
    // Rule 3: Identity & Name Queries
    else if (text.includes("name") || text.includes("who are you")) {
        response = "I am RuleBot 🤖, a simple AI assistant powered by rule-based decision logic!";
    }
    // Rule 4: Health & Mood Queries
    else if (text.includes("how are you") || text.includes("how do you do") || text.includes("how's it going")) {
        response = "I'm doing fantastic, thank you for asking! 😊 Ready to process your commands.";
    }
    // Rule 5: Capability & Help Queries
    else if (text.includes("help") || text.includes("what can you do") || text.includes("features") || text.includes("capabilities")) {
        response = "I am built using if-else decision logic! Here is what I can understand:\n• Greetings ('hello', 'hi')\n• Identity questions ('what is your name')\n• Status check ('how are you')\n• Entertainment ('tell me a joke')\n• Time check ('what time is it')\n• Exit commands ('bye', 'exit')";
    }
    // Rule 6: Entertainment / Jokes
    else if (text.includes("joke") || text.includes("funny")) {
        const jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "There are 10 types of people in the world: those who understand binary, and those who don't! 😂",
            "Why did the computer keep sneezing? It had a virus! 🤧"
        ];
        response = jokes[Math.floor(Math.random() * jokes.length)];
    }
    // Rule 7: Time & Date Queries
    else if (text.includes("time") || text.includes("clock")) {
        const now = new Date();
        response = `The current time is 🕒 ${now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}.`;
    }
    else if (text.includes("date") || text.includes("day")) {
        const now = new Date();
        response = `Today is 📅 ${now.toLocaleDateString(undefined, { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })}.`;
    }
    // Rule 8: Creator / Creator Info
    else if (text.includes("creator") || text.includes("who made you") || text.includes("built you")) {
        response = "I was created using clean HTML, CSS, JavaScript, and Python as a demonstration of rule-based AI architecture! 💻";
    }
    // Rule 9: Default Fallback (When no predefined rules match)
    else {
        response = "I'm sorry, I don't have a rule for that specific phrase yet 🤔. Try asking 'what can you do' or say 'hello'!";
    }

    // Deliver Response
    addBotMessage(response);

    // If Exit Command was triggered, terminate continuous loop session
    if (isExitCommand) {
        terminateSession();
    }
}

function addUserMessage(text) {
    const timeStr = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    const msgDiv = document.createElement('div');
    msgDiv.className = 'message user';
    msgDiv.innerHTML = `
        <div class="msg-avatar">👤</div>
        <div class="msg-content">
            <p>${escapeHTML(text)}</p>
            <div class="msg-time">${timeStr}</div>
        </div>
    `;
    chatMessages.appendChild(msgDiv);
    scrollToBottom();
}

function addBotMessage(text) {
    const timeStr = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    const msgDiv = document.createElement('div');
    msgDiv.className = 'message bot';
    
    // Replace newlines with <br> for bullet lists
    const formattedText = escapeHTML(text).replace(/\n/g, '<br>');

    msgDiv.innerHTML = `
        <div class="msg-avatar">🤖</div>
        <div class="msg-content">
            <p>${formattedText}</p>
            <div class="msg-time">${timeStr}</div>
        </div>
    `;
    chatMessages.appendChild(msgDiv);
    scrollToBottom();
}

function terminateSession() {
    isSessionActive = false;
    userInput.disabled = true;
    sendBtn.disabled = true;
    userInput.placeholder = "Session ended. Click 'Restart Session' to chat again.";
    botStatus.textContent = "Session Terminated (Exit Command Used)";
    botStatus.style.color = "#ef4444";

    const noticeDiv = document.createElement('div');
    noticeDiv.className = 'system-notice';
    noticeDiv.innerHTML = `<span>🔒 Chat loop terminated by exit command. Click 'Restart Session' to start again.</span>`;
    chatMessages.appendChild(noticeDiv);
    scrollToBottom();
}

function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function escapeHTML(str) {
    return str
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}
