# OwnAuth
Tired of using Auth apps on your mobile ? Do you trust MNCs like Google, Microsoft's Auth apps to secure your secret keys ?

Worry not, this repository helps you to make your own Serverless Auth website that can be accessible anywhere in the world only by "YOU".

### Steps to Implement
Requirements - A GitHub account & secret_keys
1. Go to this [link](https://github.com/new/import). Now copy and paste this `https://github.com/Madhukar7559/OwnAuth.git` in the <b>URL for your source repository</b>. 
2. Enter the repository name something unique so that you can only remember and set it to Private Repository.
3. Open `sec_keys.csv` file in the github itself and edit the file.
4. Clear all the entries in the CSV file.
5. In the CSV file, follow the format, `issuer_name, secret_key` and commit the file
6. Now go to settings, go to Pages in the left pane.
7. In GitHub pages, Under Build and Development, Under Source, Choose GitHub Actions, Under Static HTML, Click on Configure and Click on Commit Changes.
8. Wait for a while. Now go to GitHub Pages, and there will be a link, that is live.

Note
- Project is built using PyScript and main.py is extracted from [link](https://github.com/pyauth/pyotp/tree/develop/src/pyotp)
- <mark>This is just for experimentation. Don't use this even for personal use.<mark>


## Improvements Yet To Be Done
- [ ] better UI
- [ ] copy button
- [ ] fix padding
