<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
      <li>
      <a href="#note-about-the-requirements">Note About The Requirements</a>
      <ul>
        <li><a href="#original-requirements">Original Requirements</a></li>
      </ul>
	  <ul>
        <li><a href="#revised-requirements">Revised Requirements</a></li>
      </ul>
    </li>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- NOTE ABOUT THE REQUIREMENTS-->
## Note About The Requirements
### Original Requirements
1. The application should be able to display the exchange rate from one currency to another on either today's date or a date in the past.
2. The application should prioritize your local currency, EUR, and USD via the client UI.

### Revised Requirements
1. The currency exchange api doesn't give access to be able to process higher level api request. I revised the requirements to only process
simple currency conversion based from the latest exchange rates.
2. Same requirement applies

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ABOUT THE PROJECT -->
## About The Project

A simple currency exchange converter app.

**Back-end**
1. The back-end is created in python
2. It accepts a simple string message request ("Amount/Base Currency/Target Currency")
3. It then forms an http get request (e.g., https://v6.exchangerate-api.com/v6/64476c34684aa8f913d634c9/pair/USD/PHP)
4. Then it sends the request to exchange currency api
5. Once the response is receive it will then send the reply to the client app in the format of "Amount" + "Target Currency"

**Front-end**
1. The front-end is created in Qt creator (cross-platform)
2. It accepts an amount, base currency, and target currency from the user input
3. When the user click the convert button
3. Tt then sends a simple string message request to the back-end 
4. The message request format is in the form of "Amount/Base Currency/Target Currency" (e.g., 40/USD/PHP)
5. Once the response is receive from the backend it then displays the converted amount (e.g., 2,013.65PHP)

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [Python](https://nextjs.org/)
* [Qt Creator](https://www.qt.io/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

The application can be installed locally. Follow the simple steps below.

### Prerequisites

Install the following tools
* python3
  ```sh
  sudo apt update
  sudo apt -y upgrade
  sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
  ```
* Qt Creator
  ```sh
  https://doc.qt.io/qt-5/gettingstarted.html
  ```

### Installation

**Back-end Setup**
1. The backend can be run in any platform
2. python3 backend.py -p <port>)

**Front-end Setup**
1. Open Qt Creator
2. Open project for example: open -> path to project -> FrontEndApp.pro -> open
3. Clicked on Build -> Run

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>
