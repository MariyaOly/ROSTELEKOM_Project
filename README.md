The primary tool used for testing is Selenium, a popular browser automation framework. The tests are written in Python using the Selenium WebDriver API. The purpose of using Selenium is to automate interactions with web applications and perform end-to-end testing to ensure that different scenarios are properly handled by the application.

1. Selenium WebDriver:
Selenium WebDriver is used for automating web application testing. It provides a simple way to interact with web elements, simulate user actions, and validate expected behavior.

2. unittest Framework:
The unittest framework is a built-in Python module used for organizing and running test cases. It provides test discovery and various assertion methods for validating expected outcomes.

3. Page Object Pattern:
The Page Object Pattern is used to model the web application's pages as classes. It encapsulates the elements and interactions on each page, making the test code more modular, readable, and maintainable.

4. Explicit Waits:
Explicit waits are used from Selenium's expected_conditions to wait for specific elements to be present, clickable, or visible before proceeding with actions. This ensures that the tests wait for the necessary conditions to be met before interacting with elements.

5. Environment Variables and .env:
Environment variables and a .env file are used to store sensitive or configurable data like email addresses, passwords, and other test data. This approach ensures that sensitive data is not hardcoded in the test scripts and can be easily managed.

Why I Chosen unittest:

-Built-in: unittest is part of the Python standard library, which means it's readily available without the need for additional installations.

-Familiarity.

-Integration: If the project is closely integrated with other Python standard library modules, using unittest can result in smoother integration due to shared design principles and conventions.

-Structured.

-Compatibility: For projects that need to run on multiple Python versions.


What's Done:

The tests simulate user interactions such as clicking buttons, filling forms, and verifying displayed messages.
Explicit waits are employed to ensure that elements are present before interacting with them.
Environment variables are used to keep sensitive information separate from the code.
Overall, the tools and techniques were chosen to create robust, maintainable, and reusable test cases that cover a range of scenarios in the application under test.
