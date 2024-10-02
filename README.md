# Django-OTP-Implementation

This project demonstrates the implementation of an **OTP (One-Time Password) based login** system using Django. The OTP is valid for **1 minute**, and if the correct OTP is entered, the user is successfully logged in. If the OTP expires or is incorrect, the login fails.

## Features

- **OTP generation**: A unique OTP is generated for each login attempt.
- **1-minute OTP validity**: The OTP expires after 60 seconds.
- **Basic interface**: A minimal login form interface with OTP input.
- **Login functionality**: Success on correct OTP entry, failure otherwise.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Bootstrap for styling)
- **Database**: SQLite (default Django database)
- **Email sending**: Send OTP via email (optional)

## Basic Interface

The project includes a basic login interface where users can enter their username, password, and OTP. Bootstrap has been used for styling, but you can modify it as per your needs.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to fork this repository, create a new branch, and submit a pull request for any improvements or bug fixes!

## Query

For any query, please feel free to reach out to rajashahab912@gmail.com
