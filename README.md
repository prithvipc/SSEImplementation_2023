# SSEImplementation_2023
Implemented and tested the Curtmola scheme efficiency and vulnerabilities

This repository contains the official authors implementation associated with the paper "An In-Depth Analysis on Efficiency and Vulnerabilities on a Cloud-Based Searchable Symmetric Encryption Solution" 

Abstract: Searchable Symmetric Encryption (SSE) has come to be as an integral cryptographic approach in a world where digital privacy is essential. The capacity to search through encrypted data whilst maintaining its integrity meets the most important demand for security and confidentiality in a society that is increasingly dependent on cloud-based services and data storage. SSE offers efficient processing of queries over encrypted datasets, allowing entities to comply with data privacy rules while preserving database usability. Our research goes into this need, concentrating on the development and thorough testing of an SSE system based on the Curtmola et al. architecture and employing Advanced Encryption Standard (AES) in Cypher Block Chaining (CBC) mode. A primary goal of the research is to conduct a thorough evaluation of the security and performance of the system. In order to assess search performance, a variety of database settings were extensively tested, and the system's security was tested by simulating intricate threat scenarios such as count attacks and leakage abuse. The efficiency of operation and cryptographic robustness of the SSE system are critically examined by these reviews.

Funding: This research was not funded.

Step-by-step tutorial

This research has 4 parts:
An SSE which was built uopn the implementation of the Curtmola et al. 2006 scheme.
The same SSE returns search results in line with the search time taken on the webpage which is hosted by XAMPP.
Enron database which can be modified as per use to reduce/ add entries to test the system.
Count attack which is used on the SSE to find the number of documents relating to the keyword.

Setup:
Install python using a tutorial, for example: 'https://www.digitalocean.com/community/tutorials/install-python-windows-10'
Install the 'pycryptodome' library using 'sudo pip install pycryptodome'
Install XAMPP on system, reference: 'https://www.apachefriends.org/faq_windows.html'
Optional*: Install VSCode for user-friendly experience.

Implementation:
1. Start XAMPP and turn on Apache server for locally hosting the database (enrodThread2001). Check if localhost is active by typing 'localhost' in web browser.
2. Run the given file 'ssehash1.py' in VSCode and click on the server.
3. Search for any keyword which is present in the 'enronThread2001' file.
4. The webpage should show the results which match the keyword along with the search time taken.
5. Run the 'LAattack_try.py' in an interactive window along with the server still running.
6. It should return the number of files present on the server externally.

