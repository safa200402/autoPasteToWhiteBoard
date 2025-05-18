document.addEventListener("copy", async () => {
    try {
      const text = await navigator.clipboard.readText();
      const logs = JSON.parse(localStorage.getItem("copiedTexts") || "[]");
      logs.push(text);
      localStorage.setItem("copiedTexts", JSON.stringify(logs));
    } catch (err) {
      console.error("Gagal membaca clipboard:", err);
    }
  });
  