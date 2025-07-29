const form = document.getElementById('chat-form');
const input = document.getElementById('user-input');
const chatBox = document.getElementById('chat-box');

form.addEventListener('submit', async e => {
  e.preventDefault();
  const message = input.value.trim();
  if (!message) return;

  addMessage('user', message);
  input.value = '';
  chatBox.scrollTop = chatBox.scrollHeight;

  try {
    const res = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message }),
    });
    if (!res.ok) throw new Error('Network response was not ok');
    const data = await res.json();
    addMessage('bot', data.reply);
    chatBox.scrollTop = chatBox.scrollHeight;
  } catch (error) {
    addMessage('bot', 'Sorry, there was an error. Please try again.');
    console.error('Chat error:', error);
    chatBox.scrollTop = chatBox.scrollHeight;
  }
});

function addMessage(sender, text) {
  const messageElem = document.createElement('div');
  messageElem.classList.add('message', sender);
  messageElem.innerHTML = `<p>${escapeHtml(text)}</p>`;
  chatBox.appendChild(messageElem);
}

function escapeHtml(text) {
  const div = document.createElement('div');
  div.innerText = text;
  return div.innerHTML;
}
