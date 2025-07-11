const root = document.getElementById("root");

root.innerHTML = `
  <h3>🎬Chat with your context</h3>
  <input type="text" id="question" placeholder="Ask about this video..." style="width: 100%; padding: 5px;" />
  <button id="askBtn" style="margin-top: 8px;">Ask now</button>
  <pre id="response" style="margin-top: 10px; white-space: pre-wrap;"></pre>
  <button id="copyBtn" style="display: none; margin-top: 8px;">Copy Answer</button>
`;

document.getElementById("askBtn").addEventListener("click", () => {
  const responseElem = document.getElementById("response");
  const copyBtn = document.getElementById("copyBtn");
  
  // Simple loading animation
  let dots = 0;
  responseElem.innerText = "Loading";
  const loadingInterval = setInterval(() => {
    dots = (dots + 1) % 4;
    responseElem.innerText = "Loading" + ".".repeat(dots);
  }, 500);
  
  copyBtn.style.display = "none";

  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.tabs.sendMessage(tabs[0].id, { action: "getVideoId" }, (response) => {
      const videoId = response?.videoId;
      const question = document.getElementById("question").value;

      if (!videoId) {
        clearInterval(loadingInterval);
        responseElem.innerText = "Error: Could not get video ID. Make sure you're on a YouTube video page.";
        return;
      }

      if (!question.trim()) {
        clearInterval(loadingInterval);
        responseElem.innerText = "Error: Please enter a question.";
        return;
      }

      console.log("Sending request:", { video_id: videoId, question });

      fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ video_id: videoId, question }),
      })
        .then((res) => {
          console.log("Response status:", res.status);
          if (!res.ok) {
            throw new Error(`HTTP ${res.status}: ${res.statusText}`);
          }
          return res.json();
        })
        .then((data) => {
          clearInterval(loadingInterval);
          responseElem.innerText = data.answer || "No answer found.";
          copyBtn.style.display = "inline-block";
        })
        .catch((err) => {
          clearInterval(loadingInterval);
          console.error("Fetch error:", err);
          responseElem.innerText = "Error: " + err.message;
          copyBtn.style.display = "none";
        });
    });
  });
});

document.getElementById("copyBtn").addEventListener("click", () => {
  const responseElem = document.getElementById("response");
  const copyBtn = document.getElementById("copyBtn");
  
  navigator.clipboard.writeText(responseElem.innerText)
    .then(() => {
      copyBtn.innerText = "Copied!";
      setTimeout(() => {
        copyBtn.innerText = "Copy Answer";
      }, 2000);
    })
    .catch(err => {
      console.error('Failed to copy text: ', err);
      copyBtn.innerText = "Copy Failed";
      setTimeout(() => {
        copyBtn.innerText = "Copy Answer";
      }, 2000);
    });
});