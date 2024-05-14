document.getElementById('loginBtn').addEventListener('click', function (event) {
    event.preventDefault(); // Prevent the default form submission

    // Get the form data
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Make the API request
    fetch('http://127.0.0.1:8000/ems_log/cmp_login/', { // Replace with your DRF login endpoint
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            company_email: email,
            company_pwd: password
        }),
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => { throw new Error(err.detail || 'Login failed') });
        }
        return response.json();
    })
    .then(data => {// Assuming the API returns a token upon successful login
            // Save the token (if applicable)
            alert('Logged in successful!');

            // Redirect to a different page (if applicable)
            window.location.href = 'lghome.html';
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Error: ' + error.message);
    });
});
