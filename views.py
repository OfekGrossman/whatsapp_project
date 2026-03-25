<!DOCTYPE html>
<html lang="en">
<head>
    <title>Add Members - WhatsApp Web</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'styles.css' %}">
    <style>
        .user-list {
            max-height: 400px;
            overflow-y: auto;
            border: 1px solid var(--border-light);
            border-radius: 8px;
            margin-bottom: 20px;
        }
        .user-item {
            display: flex;
            align-items: center;
            padding: 12px;
            border-bottom: 1px solid var(--border-light);
        }
        .user-item:last-child {
            border-bottom: none;
        }
        .selection-counter {
            background-color: var(--secondary-color);
            padding: 8px 12px;
            border-radius: 4px;
            margin-bottom: 16px;
            font-size: 0.9em;
        }
        .checkbox-wrapper {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .checkbox-wrapper input[type="checkbox"] {
            width: 20px;
            height: 20px;
        }
        .warning-message {
            color: #dc3545;
            background-color: #f8d7da;
            border: 1px solid #f5c6cb;
            padding: 10px;
            border-radius: 4px;
            margin-bottom: 16px;
            text-align: center;
            display: none;
        }
        .button-group {
            display: flex;
            gap: 10px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="center-container">
        <div class="login-card" style="max-width: 600px;">
            <h2>Add Members to Group</h2>

            {% if messages %}
                {% for message in messages %}
                    <div class="error-message">{{ message }}</div>
                {% endfor %}
            {% endif %}

            <div class="warning-message" id="warningMessage">
                Please select at least one user to add to the group
            </div>

            <div class="selection-counter">
                Selected members: <span id="selectedCount">0</span>
            </div>

            <!-- Form for adding members -->
            <form method="post" action="{% url 'add_members' group.id %}" onsubmit="return validateForm()">
                {% csrf_token %}
                <div class="user-list">
                    {% for user in available_users %}
                        <div class="user-item">
                            <label class="checkbox-wrapper">
                                <input
                                    type="checkbox"
                                    name="users"
                                    value="{{ user.id }}"
                                    {% if user.id in selected_users %}checked{% endif %}
                                    onchange="updateCounter()"
                                >
                                {{ user.get_full_name|default:user.username }}
                            </label>
                        </div>
                    {% empty %}
                        <div class="user-item">No users available</div>
                    {% endfor %}
                </div>

                <div class="button-group">
                    <!-- Add Members button -->
                    <button type="submit" id="addMembersBtn" class="btn btn-primary" style="flex: 1;">Add Members</button>

                    <!-- Cancel Form -->
                    <button type="button" onclick="submitCancel()" class="btn btn-secondary" style="flex: 1;">Cancel</button>
                </div>
            </form>

            <!-- Separate hidden form for cancel action -->
            <form id="cancelForm" method="post" action="{% url 'add_members' group.id %}" style="display: none;">
                {% csrf_token %}
                <input type="hidden" name="action" value="cancel">
            </form>
        </div>
    </div>

    <script>
        function updateCounter() {
            const selectedUsers = document.querySelectorAll('input[name="users"]:checked').length;
            document.getElementById('selectedCount').textContent = selectedUsers;
            document.getElementById('warningMessage').style.display = 'none';
        }

        function validateForm() {
            const selectedUsers = document.querySelectorAll('input[name="users"]:checked').length;
            if (selectedUsers === 0) {
                document.getElementById('warningMessage').style.display = 'block';
                return false;
            }
            return true;
        }

        function submitCancel() {
            document.getElementById('cancelForm').submit();
        }

        // Initialize counter on page load
        updateCounter();
    </script>
</body>
</html>