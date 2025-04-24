document.getElementById("check-btn").addEventListener("click", () => {
    const urlInput = document.getElementById("url-input").value;
    const resultElement = document.getElementById("result");

    if (!urlInput) {
        resultElement.textContent = "Please enter a URL.";
        return;
    }

    fetch("/check", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ url: urlInput })
    })
    .then(response => response.json())
    .then(data => {
        resultElement.textContent = data.result;
    })
    .catch(error => {
        resultElement.textContent = "An error occurred. Please try again.";
        console.error(error);
    });
});