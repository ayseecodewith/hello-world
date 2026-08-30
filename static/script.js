const button = document.getElementById("helloButton");
const result = document.getElementById("result");

button.addEventListener("click", async () => {
  result.textContent = "Backend'den cevap bekleniyor...";

  try {
    const response = await fetch("/api/hello");

    const data = await response.json();

    result.textContent = data.message;
  } catch (error) {
    result.textContent = "Backend'e bağlanırken bir hata oluştu.";

    console.error(error);
  }
});
