let userLevel = null;
let chatStarted = false;
let waitingForPhoto = false;

const btn = document.getElementById("chat-btn");
const box = document.getElementById("chat-container");
const close = document.getElementById("close");
const chatTooltip = document.getElementById("chat-tooltip");
const closeTooltip = document.getElementById("closeTooltip");

if (closeTooltip) {
  closeTooltip.addEventListener("click", (e) => {
    e.stopPropagation();
    chatTooltip.style.display = "none";
  });
}

if (chatTooltip) {
  chatTooltip.addEventListener("click", () => {
    btn.click();
  });
}

const chatBody = document.getElementById("chat-body");

btn.onclick = () => {
    box.style.display = "flex";

    if (!chatStarted) {
        chatStarted = true;
        askFitnessLevel();
    }
};
function askFitnessLevel() {

    const html = `
        <div class="bot">
            <p>👋 Hey! Before we jump into workouts, what's your current fitness level?</p>

            <div class="option-buttons">
                <button onclick="selectLevel('Beginner')">Beginner</button>
                <button onclick="selectLevel('Intermediate')">Intermediate</button>
                <button onclick="selectLevel('Pro')">Pro</button>
            </div>
        </div>
    `;

    chatBody.innerHTML += html;

    chatBody.scrollTop = chatBody.scrollHeight;
}
function selectLevel(level) {

    userLevel = level;

    chatBody.innerHTML += `
        <div class="user">${level}</div>
    `;

    askPhoto();

}
function askPhoto(){

    waitingForPhoto = true;

    chatBody.innerHTML += `
        <div class="bot">
            📷 Please upload your current body condition photo.<br><br>

            This is optional and helps me personalize your workout.

            <br><br>

            <button onclick="skipPhoto()">Skip</button>
        </div>
    `;

    chatBody.scrollTop = chatBody.scrollHeight;
}
function skipPhoto(){

    waitingForPhoto = false;

    chatBody.innerHTML += `
        <div class="user">Skip</div>
    `;

    chatBody.innerHTML += `
        <div class="bot">
            Great! Now ask me anything about workouts or diet.
        </div>
    `;

}

close.onclick = () => {
  box.style.display = "none";
}

document.getElementById("message").addEventListener("keydown", (e) => {
  if (e.key === "Enter") {
    e.preventDefault();
    sendMessage();
  }
});

let pendingFile = null; // { base64, filename, mimetype }

const attachBtn = document.getElementById("attach-btn");
const fileInput = document.getElementById("file-input");
const filePreview = document.getElementById("file-preview");

attachBtn.onclick = () => {

    if(waitingForPhoto){
        fileInput.click();
    }else{
        fileInput.click();
    }

};

fileInput.addEventListener("change", () => {
  const file = fileInput.files[0];
  if (!file) return;

  if (file.size > 4 * 1024 * 1024) {
    alert("Please choose a file under 4MB.");
    fileInput.value = "";
    return;
  }

  const reader = new FileReader();
  reader.onload = () => {
    const base64 = reader.result.split(",")[1];
    pendingFile = {
      base64: base64,
      filename: file.name,
      mimetype: file.type
    };
    filePreview.style.display = "flex";
    filePreview.innerHTML = `
      <span>${file.name}</span>
      <span class="remove-file" id="remove-file">✖</span>
    `;
    document.getElementById("remove-file").onclick = () => {
      pendingFile = null;
      fileInput.value = "";
      filePreview.style.display = "none";
      filePreview.innerHTML = "";
    };
  };
  reader.readAsDataURL(file);
});




function escapeHtml(str) {
  const div = document.createElement("div");
  div.textContent = str;
  return div.innerHTML;
}

function inlineFormat(text) {
  return text.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
}

function formatReply(text) {
  const safe = escapeHtml(text);
  const rawLines = safe.split(/\n+/).map(l => l.trim()).filter(l => l.length > 0);

  let html = "";
  let inOl = false;
  let itemOpen = false;
  let inSubUl = false;
  let inTopUl = false;

  const closeSubUl = () => { if (inSubUl) { html += "</ul>"; inSubUl = false; } };
  const closeItem = () => { closeSubUl(); if (itemOpen) { html += "</li>"; itemOpen = false; } };
  const closeOl = () => { closeItem(); if (inOl) { html += "</ol>"; inOl = false; } };
  const closeTopUl = () => { if (inTopUl) { html += "</ul>"; inTopUl = false; } };

  for (let i = 0; i < rawLines.length; i++) {
    const line = rawLines[i];
    const numbered = line.match(/^\d+[\.\)]\s+(.*)/);
    const bulleted = line.match(/^[\*\-]\s+(.*)/);

    if (numbered) {
      closeTopUl();
      closeItem();
      if (!inOl) { html += "<ol>"; inOl = true; }
      html += `<li>${inlineFormat(numbered[1])}`;
      itemOpen = true;
    } else if (bulleted) {
      if (itemOpen) {
        if (!inSubUl) { html += "<ul>"; inSubUl = true; }
        html += `<li>${inlineFormat(bulleted[1])}</li>`;
      } else {
        closeOl();
        if (!inTopUl) { html += "<ul>"; inTopUl = true; }
        html += `<li>${inlineFormat(bulleted[1])}</li>`;
      }
    } else {
      closeOl();
      closeTopUl();
      const nextLine = rawLines[i + 1] || "";
      const nextIsListItem = /^\d+[\.\)]\s+/.test(nextLine) || /^[\*\-]\s+/.test(nextLine);
      if (nextIsListItem && line.length < 60) {
        html += `<p class="chat-heading">${inlineFormat(line)}</p>`;
      } else {
        html += `<p>${inlineFormat(line)}</p>`;
      }
    }
  }
  closeOl();
  closeTopUl();

  return html;
}

async function sendMessage() {
  let input = document.getElementById("message");
  let message = input.value;
  if (message == "" && !pendingFile) return;

  let userHtml = escapeHtml(message);
  if (pendingFile && pendingFile.mimetype.startsWith("image/")) {
    userHtml += `<br><img src="data:${pendingFile.mimetype};base64,${pendingFile.base64}">`;
  } else if (pendingFile) {
    userHtml += `<br>📎 ${escapeHtml(pendingFile.filename)}`;
  }

  document.getElementById("chat-body").innerHTML +=
    `<div class="user">${userHtml}</div>`;

 const payload = {
    message: message,
    level: userLevel
};

if (pendingFile) {
    payload.file = pendingFile.base64;
    payload.filename = pendingFile.filename;
    payload.mimetype = pendingFile.mimetype;
}
  

  input.value = "";
  pendingFile = null;
  fileInput.value = "";
  filePreview.style.display = "none";
  filePreview.innerHTML = "";

  document.getElementById("chat-body").innerHTML +=
    `<div class="bot" id="loading">Typing...</div>`;
  

  const response = await fetch("/ai-chat/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken
    },
    body: JSON.stringify(payload)
  });

  const data = await response.json();

  document.getElementById("loading").remove();

  document.getElementById("chat-body").innerHTML +=
    `<div class="bot">${formatReply(data.reply)}</div>`;

  document.getElementById("chat-body").scrollTop =
    document.getElementById("chat-body").scrollHeight;
}