# WhatsApp-like Messaging Application

A Django-based web application that implements user registration, authentication, and message management functionality with conversation threading support.

## Project Setup Instructions

### Required Python Version
- Python 3.8 or higher

### Installing Dependencies
1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

### Initializing the Database
1. Create database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

2. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

### Running the Development Server
1. Start the Django development server:
```bash
python manage.py runserver
```
2. Access the application at: http://127.0.0.1:8000/

## Project Structure
```
whatsapp_project/
│
├── messaging/                 # Main application directory
│   ├── static/               # Static files (CSS, JS, images)
│   ├── templates/            # HTML templates
│   │   └── messaging/
│   │       ├── registration.html
│   │       ├── login.html
│   │       ├── messages.html
│   │       └── new_message.html
│   │
│   ├── __init__.py
│   ├── admin.py             # Admin interface configuration
│   ├── apps.py              # App configuration
│   ├── forms.py             # Form definitions
│   ├── models.py            # Database models
│   ├── urls.py              # URL routing
│   └── views.py             # View functions
│
├── whatsapp/                # Project configuration directory
│   ├── __init__.py
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL routing
│   └── wsgi.py              # WSGI configuration
│
├── logs/                    # Application logs
│   └── app.log
│
├── manage.py               # Django management script
├── requirements.txt        # Project dependencies
└── README.md              # This file
```

## Feature Documentation

### User Management
- User registration with validation
- User authentication (login/logout) with form clearing functionality
- Password security with Django's auth system

### Messaging System
- Send messages to other users with length validation (max 1024 chars)
- View received messages in conversation threads
- Real-time character counter for message composition
- Clear form functionality for both new messages and replies
- Thread-based conversation view with proper scrolling
- Auto-scroll to latest message
- AJAX-based message loading and sending

### User Interface Features
- Conversation-based message organization
- Clean, WhatsApp-like interface
- Real-time character counting and validation
- Clear form functionality
- Visual feedback for message length limits

### Security Features
- CSRF protection
- Secure password handling
- Session management
- Input validation and sanitization
- Message length validation (server and client-side)

## Testing Instructions

1. Run the test suite:
```bash
python manage.py test
```

2. Manual Testing Checklist:
   - User Registration:
     - Try registering with invalid username (not starting with letter)
     - Try registering with spaces in password
     - Try registering with missing required fields
     - Test clear form functionality
   - Login:
     - Test with valid credentials
     - Test with invalid credentials
     - Verify form clearing works
   - Messaging:
     - Send message to valid user
     - Test message length limit (1024 chars)
     - Test clear button functionality
     - Verify character counter
     - Test conversation threading
     - Test reply feature
     - Verify auto-scrolling to latest message

## Known Limitations or Issues

1. Message Timestamps
   - Messages are set with a 2-hour offset from server time
   - Time zones are not fully implemented

2. UI Limitations
   - No message delivery status
   - No online/offline status
   - No real-time message updates (requires manual refresh)

3. Features Not Implemented
   - Message deletion
   - User profile management
   - Message search functionality
   - File attachments
   - Message formatting (bold, italic, etc.)

## Group Member Contributions

### Team Members
- [Student Name 1]
  - Implemented user authentication system
  - Developed message model and views
  - Created project documentation
  - Implemented conversation threading

- [Student Name 2]
  - Designed and implemented templates
  - Created forms with validation
  - Set up logging system
  - Added character counting and form clearing features

[Note: Replace [Student Name X] with actual team member names and their contributions]
