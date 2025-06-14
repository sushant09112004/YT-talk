function getYouTubeVideoId() {
  const url = window.location.href;
  const match = url.match(/v=([a-zA-Z0-9_-]{11})/);
  return match ? match[1] : null;
}
// alert("YouTube Video ID: " + getYouTubeVideoId());

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "getVideoId") {
    sendResponse({ videoId: getYouTubeVideoId() });
  }
});
