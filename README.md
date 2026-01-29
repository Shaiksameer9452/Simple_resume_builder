<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Simple Resume Builder{% endblock %}</title>

    <!-- Main CSS -->
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>

    <!-- Header -->
    <header>
        <h1>Simple Resume Builder</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/create">Create Resume</a>
        </nav>
    </header>

    <!-- Main Content -->
    <main>
        {% block content %}
        {% endblock %}
    </main>

    <!-- Footer -->
    <footer>
        <p>&copy; 2026 Simple Resume Builder </p>
    </footer>

</body>
</html>
