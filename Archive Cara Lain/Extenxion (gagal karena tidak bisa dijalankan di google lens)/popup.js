document.addEventListener("DOMContentLoaded", () => {
    const textarea = document.getElementById("clipboardText");
    const clearBtn = document.getElementById("clearBtn");
  
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      chrome.scripting.executeScript({
        target: { tabId: tabs[0].id },
        func: () => localStorage.getItem("copiedTexts"),
      }, (results) => {
        if (results && results[0].result) {
          const data = JSON.parse(results[0].result);
          textarea.value = data.join("\n");
        }
      });
    });
  
    clearBtn.addEventListener("click", () => {
      textarea.value = "";
      chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.scripting.executeScript({
          target: { tabId: tabs[0].id },
          func: () => localStorage.setItem("copiedTexts", JSON.stringify([]))
        });
      });
    });
  });
  document.getElementById("getClipboard").addEventListener("click", async () => {
    try {
      const text = await navigator.clipboard.readText();
      const existing = JSON.parse(localStorage.getItem("copiedTexts") || "[]");
      existing.push(text);
      localStorage.setItem("copiedTexts", JSON.stringify(existing));
      document.getElementById("clipboardText").value = existing.join("\n");
    } catch (err) {
      alert("Gagal membaca clipboard! Coba klik halaman dulu.");
    }
  });
  