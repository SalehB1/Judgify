# Judgify  [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa] 

Judgify is a powerful and versatile Universal Online Judge built on FastAPI. This modular system is designed for code competitions, supporting a wide range of programming languages. Its flexibility allows for easy integration of new language modules, making it a scalable solution for various coding environments.

**Note:** This repository is currently under active development and is not considered complete. Use it at your own discretion.

## Features

- **Modular System**: Judgify is built on a modular architecture, allowing easy integration of new language modules. This ensures support for virtually any programming language, making it a universal solution for code competitions.

- **FastAPI Integration**: Leveraging the speed and efficiency of FastAPI, Judgify provides a high-performance online judging platform. FastAPI's asynchronous capabilities enable quick and responsive evaluation of code submissions.

- **Scalability**: The modular design and FastAPI integration make Judgify highly scalable. Whether you're organizing a small coding competition or a large-scale event, Judgify can handle the load with ease.

## Getting Started

To set up Judgify for your code competition, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/judgify.git
   cd judgify
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Language Modules:**
   Add or write modules for the programming languages you want to support. Judgify's modular system makes it easy to extend language support.

4. **Run the Server:**
   ```bash
   python run-server.py --reload
   ```
   This will start the Judgify server, and it will be ready to handle code submissions.

5. **Integrate with Your Platform:**
   Integrate Judgify into your coding platform by making API requests for code evaluation. Refer to the API documentation for details on how to interact with the Judgify server.

## Contributing

Judgify welcomes contributions from the community. If you'd like to add support for a new programming language or improve existing features, please check out the [contribution guidelines](CONTRIBUTING.md).

## License

This Project is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

## Contact

For any questions or inquiries, feel free to contact us at (mailto:salehwork07@gmail.com).

Happy coding with Judgify!
