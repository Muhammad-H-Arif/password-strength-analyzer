let ws = new WebSocket("ws://localhost:8000/ws");

ws.onmessage = function(event) {
    let feedback = document.getElementById("feedback");
    let strengthBar = document.getElementById("passwordStrengthBar");

    feedback.innerText = event.data;

    // Update progress bar based on feedback
    if (event.data.includes("Weak")) {
        strengthBar.style.width = "25%";
        strengthBar.style.backgroundColor = "#ff0000"; // Red for weak
    } else if (event.data.includes("Strong")) {
        strengthBar.style.width = "100%";
        strengthBar.style.backgroundColor = "#00ff00"; // Green for strong
    } else {
        strengthBar.style.width = "50%";
        strengthBar.style.backgroundColor = "#ffff00"; // Yellow for average
    }
};

function checkPassword() {
    let password = document.getElementById("passwordInput").value;
    ws.send(password);
}

function togglePasswordVisibility() {
    let passwordInput = document.getElementById("passwordInput");
    let togglePassword = document.getElementById("togglePassword");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        togglePassword.classList.remove("fa-eye");
        togglePassword.classList.add("fa-eye-slash");
    } else {
        passwordInput.type = "password";
        togglePassword.classList.remove("fa-eye-slash");
        togglePassword.classList.add("fa-eye");
    }
}
