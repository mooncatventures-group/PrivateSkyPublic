 # Updated Flask Code with Decryption

This repository contains a Flask-based application that demonstrates positional encoding, narrative generation, and message decryption. The implementation follows the Sub-Lex protocol and includes functionality for encoding plaintext into a narrative and decrypting encoded messages back into plaintext.

## Features
- Flask API for encoding and decoding messages.
- AES-256 encryption with hex remapping for narrative-friendly character sets.
- Decryption endpoint to reconstruct the original message.

## Installation
### Prerequisites
- Python 3.8 or higher
- `pip` package manager

### Dependencies
Install the required dependencies using `pip`:
pip install Flask pycryptodome

## Usage
### Starting the Flask Application
1. Clone the repository:
   git clone https://github.com/your-username/updated-flask-decryption.git
   cd updated-flask-decryption
2. Run the Flask application:
   python app.py
3. Access the API at `http://127.0.0.1:5000`.

### API Endpoints
#### 1. Encode a Message
   Endpoint: `/encode`  
   Method: POST  

   Request Body:
   {
       "message": "We are meeting at 9 at 2403 Wayne."
   }
   Response:
   {
       "narrative": "We are seeing at Wayne later tonight at 9.",
       "result_table": {
           "a": 5,
           "t": 12,
           "W": 9,
           ...
       }
   }

#### 2. Decode a Narrative
   Endpoint: `/decode`  
   Method: POST  

   Request Body:
   {
       "narrative": "We are seeing at Wayne later tonight at 9.",
       "key": "Itookmydogforawalkinthepark!"
   }
   Response:
   {
       "original_message": "We are meeting at 9 at 2403 Wayne."
   }

## Sample Input and Output
### Input (Encoding)
Message:
We are meeting at 9 at 2403 Wayne.
Output
Narrative:
We are seeing at Wayne later tonight at 9.
Result Table:
{
    "a": 5,
    "t": 12,
    "W": 9,
    ...
}

### Input (Decoding)
Narrative:
We are seeing at Wayne later tonight at 9.
Decryption Key:
Itookmydogforawalkinthepark!
Output
Original Message:
We are meeting at 9 at 2403 Wayne.

## License
This project is licensed under the Apache License 2.0. 

### Key Terms
1. Freedom to Use, Modify, and Distribute: You are free to use, modify, and distribute this code for both personal and commercial purposes.
2. Attribution Required: You must include proper attribution to the original author in derivative works.
3. Patent Grant: The license includes a grant of patent rights from contributors (You may not patent this code in full or in part) , protecting against patent claims on the software.
4. Limitations: The Apache License 2.0 does not grant permission to use proprietary components (e.g., audiobook-related extensions) that are reserved as private intellectual property by the author. Custom implementations and extensions beyond this base repository may be subject to additional licensing terms.

For full license details, see the LICENSE file in the repository.

## Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## Contact
As noted on project 
