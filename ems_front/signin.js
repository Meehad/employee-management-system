document.getElementById("submitBtn").addEventListener("click", function(event) {
    event.preventDefault(); // Prevent the default form submission

    const companyName = document.getElementById("companyName").value;
    const email = document.getElementById("email").value;
    const contactNumber = document.getElementById("contactNumber").value;
    const password = document.getElementById("pwd").value;
    const confirmPassword = document.getElementById("confirm").value;

    if (password !== confirmPassword) {
        alert("Password and confirm password must be the same");
        return;
    }
    
    if (password.length < 8) {
        alert("Password must be greater than 8 characters");
        return;
    }

    // Make the API request
    fetch('http://127.0.0.1:8000/ems_log/cmp_reg/', { // Replace with your DRF registration endpoint
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            company_name: companyName,
            company_email: email,
            company_contact: contactNumber,
            company_pwd: password
        }),
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => { throw err; });
        }
        return response.json();
    })
    .then(data => {
        alert('Registration successful!');
        window.location.href = 'login.html';
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Registration failed: ' + JSON.stringify(error));
    });
});
