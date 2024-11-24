# Finger-User-Enumeration
Finger User Enumeration is a Python script that allows you to identify users of system through finger protocol.

![image](https://github.com/user-attachments/assets/0869c753-9b99-4977-a216-bdd81264d5ea)

## Requirements

- Python 3.x
- pyfiglet library (installable via `pip install pyfiglet`)

## Download

On the repository page, click on the "Code" button located near the top-right corner. This will open a dropdown menu with a few options. Select "Download ZIP" to download the repository as a ZIP file. Or use following command via terminal:

```
git clone https://github.com/dev-angelist/finger_user_enumeration
```

## Download Wordlist

You can download a usernames wordlist from SecLists:

```
wget -O names.txt https://raw.githubusercontent.com/danielmiessler/SecLists/master/Usernames/Names/names.txt
```     

If you're using Kali Linux, the wordlist is already available at this path:
        
```
/usr/share/wordlists/wfuzz/others/names.txt
```
## Usage

To perform a user enumeration on a target:

```
python3 finger_user_enumeration.py -t <target> -w <wordlist> [-p <port>]
```
[Video del 2024-11-24 20-21-18.webm](https://github.com/user-attachments/assets/efe86211-706f-43eb-be1c-8ce8d79c4e1c)

### Viewing Help

To display help with available options:

```
python3 finger_user_enumeration -h
```
![image](https://github.com/user-attachments/assets/11c60711-0d1e-4914-9a61-f5fe2b5a8dfd)

## Contributing

If you wish to contribute to this project, follow these steps:

1. Fork this repository.
2. Create a branch for your contribution (`git checkout -b feature/your-contribution`).
3. Commit your changes (`git commit -am 'Add feature X'`).
4. Push your branch (`git push origin feature/your-contribution`).
5. Open a pull request.

## Author

@dev-angelist ([GitHub profile](https://github.com/dev-angelist)) 

## Legal Disclaimer

Please note that conducting port scanning activities may be illegal in some jurisdictions without proper authorization. Before using this tool, ensure that you have the necessary permissions to perform scanning activities on the target network. Unauthorized port scanning can potentially violate laws and regulations related to computer security and privacy.

It is your responsibility to comply with all applicable laws and regulations in your jurisdiction. The author of this script does not condone or endorse any illegal or unauthorized use of this tool.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
