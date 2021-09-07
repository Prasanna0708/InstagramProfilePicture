import instaloader
image = instaloader.Instaloader()
display_picture = input("Enter insta user name: ")
image.download_profile(display_picture,profile_pic_only=True)