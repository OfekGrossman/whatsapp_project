<!DOCTYPE html>
<html lang="en">
<head>
    <title>Create New Group - WhatsApp Web</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'styles.css' %}">
    <style>
        .errorlist {
            color: red;
            list-style: none;
            padding: 0;
            margin: 5px 0;
            font-size: 14px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        textarea, input {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }

        textarea {
            min-height: 100px;
            resize: vertical;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }

        .char-count {
            font-size: 12px;
            color: #666;
            margin-top: 4px;
            text-align: right;
        }
    </style>
</head>
<body>
    <div class="center-container">
        <div class="login-card" style="max-width: 500px;">
            <h2>Create New Group</h2>

            <form method="post">
                {% csrf_token %}

                <div class="form-group">
                    <label for="id_name">Group Name</label>
                    <input
                        type="text"
                        name="name"
                        id="id_name"
                        placeholder="Enter group name"
                        {% if form.name.value %}value="{{ form.name.value }}"{% endif %}
                    >
                    <div class="char-count" id="name-counter">0/38</div>
                    {{ form.name.errors }}
                </div>

                <div class="form-group">
                    <label for="id_description">Description</label>
                    <textarea
                        name="description"
                        id="id_description"
                        placeholder="Enter group description"
                    >{% if form.description.value %}{{ form.description.value }}{% endif %}</textarea>
                    <div class="char-count" id="desc-counter">0/255</div>
                    {{ form.description.errors }}
                </div>

                <div class="button-group" style="display: flex; gap: 10px;">
                    <button type="submit" class="btn btn-primary" style="flex: 1;">Create Group</button>
                    <a href="{% url 'messages' %}" class="btn btn-secondary" style="flex: 1; text-align: center; padding: 12px;">Cancel</a>
                </div>
            </form>
        </div>
    </div>

    <script>
        // Character counter for name
        const nameInput = document.getElementById('id_name');
        const nameCounter = document.getElementById('name-counter');

        nameInput.addEventListener('input', function() {
            const count = this.value.length;
            nameCounter.textContent = `${count}/38`;
        });

        // Character counter for description
        const descInput = document.getElementById('id_description');
        const descCounter = document.getElementById('desc-counter');

        descInput.addEventListener('input', function() {
            const count = this.value.length;
            descCounter.textContent = `${count}/255`;
        });

        // Initialize counters
        nameCounter.textContent = `${nameInput.value.length}/38`;
        descCounter.textContent = `${descInput.value.length}/255`;
    </script>
</body>
</html>