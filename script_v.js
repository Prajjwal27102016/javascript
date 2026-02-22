function validate(e) {
    e.preventDefault();

    const email = document.getElementById('email').value;
    const pass = document.getElementById('password').value;
    const age = document.getElementById('age').value;

    let message = '';

    if (email === '') {
        message = 'Enter an email.';
    } else if (pass === '') {
        message = 'Enter a password.';
    } else if (age === '') {
        message = 'Enter your age.';
    } else {
        message = 'Login successful!';
    }

    document.getElementById('message').innerText = message;
}