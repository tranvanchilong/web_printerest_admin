SESSION_SECRET_KEY = '2jjggsj00wa45asdejlkj'
SESSION_MAX_AGE = 60 * 60 * 24 * 7
JWT_SECRET_KEY = '4534HN&*j12h0asdejlkj'
JWT_ALGORITHM = 'HS256'
JWT_MAX_AGE = 60 * 60 * 24 * 3
JWT_MAX_AGE_REMEMBER_ME = 60 * 60 * 24 * 47
DEBUG = True

# config database
DB = {
    "DB_HOST": "mongodb://adminmg:tM5Jngh9EbKu@5.161.176.184:27018/admin",
    "DB_NAME": "pinterest",
    "COL_DATA": "data",
    "DB_col_set" :"lang_demo",

    # "DB_HOST": "mongodb://host.docker.internal:3000/admin",
    # "DB_NAME": "starlette_test",
    "COL_USERS": "users",
    "COL_ROUTES": "routes",
    "COL_GROUPS": "groups"
}
USERS = [
    {
        "username": "admin", 
        "password": "vanthethoi",
        "groups": ["dev"]
    }
]

# Noti
telegram_head = "[AntC Analytics]"

# website setting
SITE_NAME = "Admin"
# THEME = "coin_theme"
THEME = "pin_theme"



posts2 = {
    "type": "template_page",
    "lang_status": "True",
    "name": "home",
    "handle": "",


    # "tran_handle": {
    #     "source": "submit",
    #     "tran": "submit",
    # },
    "content":{
        "title":{
                "source": "Download Whatever You Want",
                "tran": "Download Whatever You Want",
            }, 
        "tools":{
                "source": "Tools",
                "tran": "Tools",
            }, 
        "main_language":{
                "source": "Language",
                "tran": "Language",
            },
        "button":{
                "source":  "Download",
                "tran": "Download",
            },
        "language":{
                "source":  "en",
                "tran": "en",
            },

        "intro_title":{
            "source": "What is a video downloader?",
            "tran": "What is a video downloader?",
        },
        
        "intro_content_first":{
            "source": "english" ,
            "tran": "english" ,
            },
        "intro_content_mid":{
            "source": ["english","english","english"],
            "tran": ["english","english","english"],
            },
        "intro_content_last":{
            "source": "english",
            "tran": "english",
        }, 
        
        

        "step_title":{
            "source": "Steps to download videos",
            "tran": "Steps to download videos",
        },

        "step_step_1_first":{
            "source": "STEP 1" ,
            "tran": "STEP 1" ,
            },
        "step_step_1_mid":{
            "source": "english" ,
            "tran": "english" ,
            },
        "step_step_1_last":{
            "source": "english",
            "tran": "english",
            }, 

        
        "step_step_2_first":{
            "source": "STEP 2" ,
            "tran": "STEP 2" ,
        },
        "step_step_2mid":{
            "source": "english" ,
            "tran": "english" ,
        }, 
        "step_step_2_last":{
            "source":  "english",
            "tran": "english",
        },
        

        "step_step_3_first":{
            "source": "STEP 3" ,
            "tran": "STEP 3" ,
        },
        "step_step_3_mid":{
            "source": "english" ,
            "tran": "english" ,
        }, 
        "step_step_3_last":{
            "source": "english",
            "tran": "english",
        }, 
        
    

        "Q_A_title":{
            "source": "Frequently asked questions",
            "tran": "Frequently asked questions",
        },
        "Q_A_Q1":{
            "source": "Do I need to sign up for an account to download videos on Pinterest Downloader?",
            "tran": "Do I need to sign up for an account to download videos on Pinterest Downloader?",
        },
        "Q_A_A1":{
            "source": "No, you don't need to sign up for an account to download videos, images or Gifs.",
            "tran": "No, you don't need to sign up for an account to download videos, images or Gifs.",
        }, 
        "Q_A_Q2":{
            "source": "Where are Pinterest videos saved after being downloaded?",
            "tran": "Where are Pinterest videos saved after being downloaded?",
        }, 
        "Q_A_A2":{
            "source": "Your browser will ask you for the default folder where you want to download these videos before the download begins. ",
            "tran": "Your browser will ask you for the default folder where you want to download these videos before the download begins. ",
        }, 
        "Q_A_Q3":{
            "source": "Is Pinterest video download completely free?",
            "tran": "Is Pinterest video download completely free?",
        }, 
        "Q_A_A3":{
            "source": "Yes, you don't have to pay anything because the Pinterest Downloader website is always free.",
            "tran": "Yes, you don't have to pay anything because the Pinterest Downloader website is always free.",
        }, 
        
    }

}



posts2_2 = {
    "type": "template_post",
    "lang_status": "True",
    "name": "About us",
    "handle": "about-us",
    "tran_name": {
        "source": "About us",
        "tran": "About us",
    },

    "tran_handle": {
        "source": "about-us",
        "tran": "about-us",
    },
    "content": {
        "source": '<div id="container" class="container pt-4"><div><div class="row"><div class="col-12 col-xl-10 mx-auto"><div class="post "><h1>About us                        </h1><p>Pinterestdownloader.io is a free Pinterest downloader that allows you to download all Pinterest videos and images for immediate use on your laptop, PC, and mobile phone.                        </p><h2>Our mission</h2><p>Our mission is to provide this free tool to users all over the world. Therefore, our team came up with the idea of ​​“Easy to use for everyone and remove the language barrier”, Pinterestdownloader.io will do our best to translate the website into more than 20 widely used languages best in the world.                        </p><h2>Contact us                        </h2><p>If you find our tool is not running as expected. Please let us know via our official email: contact@downloadpinterest.io or send us a message here.                        </p><img src="https://pinterestdownloader.io/assets/img/about-us.jpg" width="100%" alt=""></div></div></div></div></div>',

        "tran": '<div id="container" class="container pt-4"><div><div class="row"><div class="col-12 col-xl-10 mx-auto"><div class="post "><h1>About us                        </h1><p>Pinterestdownloader.io is a free Pinterest downloader that allows you to download all Pinterest videos and images for immediate use on your laptop, PC, and mobile phone.                        </p><h2>Our mission</h2><p>Our mission is to provide this free tool to users all over the world. Therefore, our team came up with the idea of ​​“Easy to use for everyone and remove the language barrier”, Pinterestdownloader.io will do our best to translate the website into more than 20 widely used languages best in the world.                        </p><h2>Contact us                        </h2><p>If you find our tool is not running as expected. Please let us know via our official email: contact@downloadpinterest.io or send us a message here.                        </p><img src="https://pinterestdownloader.io/assets/img/about-us.jpg" width="100%" alt=""></div></div></div></div></div>',
    },
}


posts2_3 = {
    "type": "template_post",
    "lang_status": "True",
    "name": "contact",
    "handle": "contact",
    "tran_name": {
        "source": "Contact Us",
        "tran": "Contact Us",
    },

    "tran_handle": {
        "source": "contact",
        "tran": "contact",
    },
    "content": {
        "source": '<div id="container" class="container pt-4"><div class="row"><div class="col-xl-10 mx-auto mb-4"><div class="row"><div class="col-xl-6"><div class="post-content mt-4"><h1>Contact Us</h1><p>If you encounter any difficulties or questions while using our tool, do not hesitate to contact our team for the most timely support.</p><p>Do not hesitate to contact us; we will get back to you as soon as possible. Please double-check our terms of service to avoid errors.                            </p><p>Contact us via                            </p><form method="POST" action=""><div class="row"><div class="col-lg-6 mb-3"><label for="your-name" class="fw-500">Your Name :</label><input type="text" name="input[name]" class="form-control fs-14 form-input-custom" id="your-name" placeholder="Your Name" required=""></div><div class="col-lg-6 mb-3"><label for="email" class="fw-500">Your Email :</label><input type="email" name="input[email]" class="form-control fs-14 form-input-custom" id="email" placeholder="Your Email" required=""></div><div class="col-12 mb-3"><label for="content" class="fw-500">Your Message :</label><textarea class="form-control fs-14 form-input-custom" name="input[message]" id="content" rows="3" placeholder="Questions or Comments" required=""></textarea></div><div class="col-12 mb-3 d-flex"><button type="submit" name="btn-send" value="submit" class="btn btn-primary col-xl-4 me-auto mx-auto">Send                                        </button></div></div></form></div></div><div class="col-xl-6"><div class="post-content"><img src="https://pinterestdownloader.io/assets/img/contact-us.jpg" alt="" style="width:100%"></div></div></div></div></div></div>',

        "tran": '<div id="container" class="container pt-4"><div class="row"><div class="col-xl-10 mx-auto mb-4"><div class="row"><div class="col-xl-6"><div class="post-content mt-4"><h1>Contact Us</h1><p>If you encounter any difficulties or questions while using our tool, do not hesitate to contact our team for the most timely support.</p><p>Do not hesitate to contact us; we will get back to you as soon as possible. Please double-check our terms of service to avoid errors.                            </p><p>Contact us via                            </p><form method="POST" action=""><div class="row"><div class="col-lg-6 mb-3"><label for="your-name" class="fw-500">Your Name :</label><input type="text" name="input[name]" class="form-control fs-14 form-input-custom" id="your-name" placeholder="Your Name" required=""></div><div class="col-lg-6 mb-3"><label for="email" class="fw-500">Your Email :</label><input type="email" name="input[email]" class="form-control fs-14 form-input-custom" id="email" placeholder="Your Email" required=""></div><div class="col-12 mb-3"><label for="content" class="fw-500">Your Message :</label><textarea class="form-control fs-14 form-input-custom" name="input[message]" id="content" rows="3" placeholder="Questions or Comments" required=""></textarea></div><div class="col-12 mb-3 d-flex"><button type="submit" name="btn-send" value="submit" class="btn btn-primary col-xl-4 me-auto mx-auto">Send                                        </button></div></div></form></div></div><div class="col-xl-6"><div class="post-content"><img src="https://pinterestdownloader.io/assets/img/contact-us.jpg" alt="" style="width:100%"></div></div></div></div></div></div>',
    },
}




posts2_4 = {
    
    "type": "template_post",
    "lang_status": "True",
    "name": "Terms and conditions",
    "handle": "terms-conditions",
    "tran_name": {
        "source": "Terms and conditions",
        "tran": "Terms and conditions",
    },

    "tran_handle": {
        "source": "terms-conditions",
        "tran": "terms-conditions",
    },
    "content": {
        "source": '<div id="container" class="container pt-4"><div><div class="row"><div class="col-12 col-xl-10 mx-auto "><div class="post-content"><h1>Terms and conditions</h1><p>Please read these terms of service (Terms of Service or ToS) carefully before accessing our application and website.</p><p>Our ToS may change from time to time to be in line with the developments to our application and website to give our valued users the highest satisfaction. Please check regularly the update time on top of the ToS to ensure you have read the updated version with changes.</p><p>Words with the first letter capitalized have the meaning defined in the following conditions. The following definitions will have the same meaning regardless of whether they occur in the singular or plural.</p><h2>Define</h2><p>For the purposes of these Terms and Conditions:</p><ul><li>Country mentioned: Vietnam</li><li>Company (referred to as "The Company", "We", "We" or "Our" in this Agreement) refers to Pinterestdownloader.io.</li><li>The term “device” means any device that can access the Service such as a computer, mobile phone or digital tablet.</li><li>Terms and Conditions (also known as the "Terms") means these Terms and Conditions forming the entire agreement between You and the Company regarding the use of the Service.</li><li>Third party social media service means any service or content (including data, information, products or services) provided by a third party that may be displayed, including or provided by the Service.</li><li>The site refers to Pinterest Downloader, accessible from https://pinterestdownloader.io.</li><li>You mean the individual accessing or using the Service, or the company or other entity acting on behalf of that individual accessing or using the Service, as applicable.</li></ul><h2>Acceptance of Terms of Service</h2><p>By accessing and using our application and website, you signify your acceptance of our policy and ToS, including the updated versions. If you do not agree with any content, please do not use our application and website.</p><h2>Who may use our Services (User)</h2><p>Our ToS governs the relationship between Pinterest Downloader application (Pinterest Downloader App) and users of Pinterest Downloader App being who access the Pinterest Downloader App and/or use the products and services provided through the Pinterest Downloader App (Pinterest Downloader Products and Services).</p><p>By accessing or using Pinterest Downloader Products and Services, you confirm that you have carefully read, understood and accepted our ToS, and you agree to abide by the ToS as a User/Users</p><p>Our ToS is a mutual agreement between you, either an individual or an entity (You or User) or a group of individuals or entities (You or Users), and the developer of Pinterest Downloader Products and Services (Pinterest Downloader) regarding the use of Pinterest Downloader Products and Services</p><h2>Materials relate to our Services</h2><p>Pinterest Downloader creates and develops content, information, graphics, documents, text, products, and all other elements and products and services offered through Pinterest Downloader App (Content or Materials) available for your use for free and personal use subject to the terms and conditions set out in this document.</p><p>By accessing and using Pinterest Downloader App you agree to be bound by and to accept our ToS and all terms and conditions contained and/or referenced herein, and you agree to abide by the ToS as a User/Users of our Content and Materials.</p><h2> {Users} Obligations</h2><p>You agree to use Pinterest Downloader Tool, Pinterest Downloader Products and Services only for purposes permitted by our ToS as well as any applicable law, regulation or generally accepted practices or guidelines in the relevant jurisdictions.</p><p>Pinterest Downloader IS NOT RESPONSIBLE FOR ANY VIOLATION OF APPLICABLE LAWS, RULES, OR REGULATIONS COMMITTED BY YOU OR A THIRD PARTY AT YOUR BEHEST.</p><h2>Intellectual Property</h2><p>Users are responsible for the content you use with (the link you paste on) Pinterest Downloader App.</p><ul><li>We only display "original" content that users have posted on websites, pages or networks of service or social network providers. Users are responsible for ensuring they have the legal right in accordance with relevant laws and ensure their own intellectual property rights in relation to the content as posted.</li><li>Users only use video downloaded through the Pinterest Downloader App for personal, non-commercial, free purposes.</li><li>Pinterest Downloader cannot and has no obligation to check whether each content/information is legal or not, but if it detects any violation, it will ban Users from accessing and using Pinterest Downloader App and Pinterest Downloader Products and Services.</li><li>Pinterest Downloader does not backup/archive Users’ content for any reason.</li><li>We encourage and thank you who inform us of any suspect misuse, misrepresentation, unauthorized use, infringement and non-compliance for our proper handling.</li><li>Users are responsible for the content you use with (the link you paste on) Pinterest Downloader App.</li><li>Pinterest Downloader provides support to Users to download information/content Users paste on Pinterest Downloader App and Web for the legitimate interests of the Users.</li></ul><h2>Use License</h2><p>We grant our Users permission to temporarily download one copy of the Content and Materials (as defined above) on Pinterest Downloader App for personal, non-commercial transitory viewing only. This is the grant of a license, not a transfer of title, and under this license you may not:</p><ul><li>Alter, modify, distribute or duplicate the Materials;</li><li>Use the Content and Materials for any commercial purpose, or for any public display (commercial or non-commercial);</li><li>Remove any copyright or other proprietary notations from the Content and Materials; or transfer the Content and Materials to another person or "mirror" the Content and Materials on any other server.</li><li>Transfer the Content and Materials to another person or "mirror" the Content and Materials on any other server.</li></ul><h2>Disclaimer</h2><p>We respect and assist Users in protecting their legitimate rights of attribution and integrity in works and contents. The Content and Materials on Pinterest Downloader App are provided to serve the interest of the Users who are the legitimate owners or authors. Pinterest Downloader makes no warranties, expressed or implied, and hereby disclaims and negates all other warranties, including without limitation, implied warranties or conditions of merchantability, fitness for a particular purpose, or non-infringement of intellectual property or other violation of rights. Further, Pinterest Downloader does not warrant or make any representations concerning the accuracy, likely results, or reliability of the use of the Content and Materials on its website or otherwise relating to such Content and Materials or on any sites linked to the site.</p><h2>Privacy</h2><p>We run Pinterest Downloader App in compliance with our set principles to ensure that the confidentiality of personal information including information of our Users is protected and maintained without disclosing to any third parties for any reason.</p><h2>Accuracy of Content and Materials</h2><p>The Content and Materials appearing on Pinterest Downloader App could include technical, typographical, or photographic errors. Pinterest Downloader does not warrant that any of the Content and Materials are accurate, complete, or current. Pinterest Downloader may make changes to the Content and Materials contained on its website at any time without notice.</p><h2>Links</h2><p>Pinterest Downloader has no responsibility for any of the sites linked to its website, together with the contents thereof. The inclusion of any link does not imply endorsement by Pinterest Downloader of the site. Use of any such linked website is at the Users own risk.</p><h2>Terms of Use - Modifications</h2><p>These Terms of Service may be amended by Pinterest Downloader at any time upon notice provided by any of the following means: through a posting on the main page of the Website, when or after you login into your User Account (as defined below), or by e-mail to the address you provided when you set up your User Account. We always add information on the updated version of the Terms of Service on the top of the terms. Therefore, you are responsible for reading the updated terms every time you access/use our Services and ensure you are fully aware of the terms/updates before using our Services. Your failure to provide or maintain accurate or current contact information in your User Account will not obviate your responsibility to comply with these Terms of Service as amended from time to time. Using contact details or identifications of others is not allowed and is considered fraud. We will deactivate your account at any time we identify your fraud.</p></div></div></div></div></div>',

        "tran": '<div id="container" class="container pt-4"><div><div class="row"><div class="col-12 col-xl-10 mx-auto "><div class="post-content"><h1>Terms and conditions</h1><p>Please read these terms of service (Terms of Service or ToS) carefully before accessing our application and website.</p><p>Our ToS may change from time to time to be in line with the developments to our application and website to give our valued users the highest satisfaction. Please check regularly the update time on top of the ToS to ensure you have read the updated version with changes.</p><p>Words with the first letter capitalized have the meaning defined in the following conditions. The following definitions will have the same meaning regardless of whether they occur in the singular or plural.</p><h2>Define</h2><p>For the purposes of these Terms and Conditions:</p><ul><li>Country mentioned: Vietnam</li><li>Company (referred to as "The Company", "We", "We" or "Our" in this Agreement) refers to Pinterestdownloader.io.</li><li>The term “device” means any device that can access the Service such as a computer, mobile phone or digital tablet.</li><li>Terms and Conditions (also known as the "Terms") means these Terms and Conditions forming the entire agreement between You and the Company regarding the use of the Service.</li><li>Third party social media service means any service or content (including data, information, products or services) provided by a third party that may be displayed, including or provided by the Service.</li><li>The site refers to Pinterest Downloader, accessible from https://pinterestdownloader.io.</li><li>You mean the individual accessing or using the Service, or the company or other entity acting on behalf of that individual accessing or using the Service, as applicable.</li></ul><h2>Acceptance of Terms of Service</h2><p>By accessing and using our application and website, you signify your acceptance of our policy and ToS, including the updated versions. If you do not agree with any content, please do not use our application and website.</p><h2>Who may use our Services (User)</h2><p>Our ToS governs the relationship between Pinterest Downloader application (Pinterest Downloader App) and users of Pinterest Downloader App being who access the Pinterest Downloader App and/or use the products and services provided through the Pinterest Downloader App (Pinterest Downloader Products and Services).</p><p>By accessing or using Pinterest Downloader Products and Services, you confirm that you have carefully read, understood and accepted our ToS, and you agree to abide by the ToS as a User/Users</p><p>Our ToS is a mutual agreement between you, either an individual or an entity (You or User) or a group of individuals or entities (You or Users), and the developer of Pinterest Downloader Products and Services (Pinterest Downloader) regarding the use of Pinterest Downloader Products and Services</p><h2>Materials relate to our Services</h2><p>Pinterest Downloader creates and develops content, information, graphics, documents, text, products, and all other elements and products and services offered through Pinterest Downloader App (Content or Materials) available for your use for free and personal use subject to the terms and conditions set out in this document.</p><p>By accessing and using Pinterest Downloader App you agree to be bound by and to accept our ToS and all terms and conditions contained and/or referenced herein, and you agree to abide by the ToS as a User/Users of our Content and Materials.</p><h2>Users Obligations</h2><p>You agree to use Pinterest Downloader Tool, Pinterest Downloader Products and Services only for purposes permitted by our ToS as well as any applicable law, regulation or generally accepted practices or guidelines in the relevant jurisdictions.</p><p>Pinterest Downloader IS NOT RESPONSIBLE FOR ANY VIOLATION OF APPLICABLE LAWS, RULES, OR REGULATIONS COMMITTED BY YOU OR A THIRD PARTY AT YOUR BEHEST.</p><h2>Intellectual Property</h2><p>Users are responsible for the content you use with (the link you paste on) Pinterest Downloader App.</p><ul><li>We only display "original" content that users have posted on websites, pages or networks of service or social network providers. Users are responsible for ensuring they have the legal right in accordance with relevant laws and ensure their own intellectual property rights in relation to the content as posted.</li><li>Users only use video downloaded through the Pinterest Downloader App for personal, non-commercial, free purposes.</li><li>Pinterest Downloader cannot and has no obligation to check whether each content/information is legal or not, but if it detects any violation, it will ban Users from accessing and using Pinterest Downloader App and Pinterest Downloader Products and Services.</li><li>Pinterest Downloader does not backup/archive Users’ content for any reason.</li><li>We encourage and thank you who inform us of any suspect misuse, misrepresentation, unauthorized use, infringement and non-compliance for our proper handling.</li><li>Users are responsible for the content you use with (the link you paste on) Pinterest Downloader App.</li><li>Pinterest Downloader provides support to Users to download information/content Users paste on Pinterest Downloader App and Web for the legitimate interests of the Users.</li></ul><h2>Use License</h2><p>We grant our Users permission to temporarily download one copy of the Content and Materials (as defined above) on Pinterest Downloader App for personal, non-commercial transitory viewing only. This is the grant of a license, not a transfer of title, and under this license you may not:</p><ul><li>Alter, modify, distribute or duplicate the Materials;</li><li>Use the Content and Materials for any commercial purpose, or for any public display (commercial or non-commercial);</li><li>Remove any copyright or other proprietary notations from the Content and Materials; or transfer the Content and Materials to another person or "mirror" the Content and Materials on any other server.</li><li>Transfer the Content and Materials to another person or "mirror" the Content and Materials on any other server.</li></ul><h2>Disclaimer</h2><p>We respect and assist Users in protecting their legitimate rights of attribution and integrity in works and contents. The Content and Materials on Pinterest Downloader App are provided to serve the interest of the Users who are the legitimate owners or authors. Pinterest Downloader makes no warranties, expressed or implied, and hereby disclaims and negates all other warranties, including without limitation, implied warranties or conditions of merchantability, fitness for a particular purpose, or non-infringement of intellectual property or other violation of rights. Further, Pinterest Downloader does not warrant or make any representations concerning the accuracy, likely results, or reliability of the use of the Content and Materials on its website or otherwise relating to such Content and Materials or on any sites linked to the site.</p><h2>Privacy</h2><p>We run Pinterest Downloader App in compliance with our set principles to ensure that the confidentiality of personal information including information of our Users is protected and maintained without disclosing to any third parties for any reason.</p><h2>Accuracy of Content and Materials</h2><p>The Content and Materials appearing on Pinterest Downloader App could include technical, typographical, or photographic errors. Pinterest Downloader does not warrant that any of the Content and Materials are accurate, complete, or current. Pinterest Downloader may make changes to the Content and Materials contained on its website at any time without notice.</p><h2>Links</h2><p>Pinterest Downloader has no responsibility for any of the sites linked to its website, together with the contents thereof. The inclusion of any link does not imply endorsement by Pinterest Downloader of the site. Use of any such linked website is at the Users own risk.</p><h2>Terms of Use - Modifications</h2><p>These Terms of Service may be amended by Pinterest Downloader at any time upon notice provided by any of the following means: through a posting on the main page of the Website, when or after you login into your User Account (as defined below), or by e-mail to the address you provided when you set up your User Account. We always add information on the updated version of the Terms of Service on the top of the terms. Therefore, you are responsible for reading the updated terms every time you access/use our Services and ensure you are fully aware of the terms/updates before using our Services. Your failure to provide or maintain accurate or current contact information in your User Account will not obviate your responsibility to comply with these Terms of Service as amended from time to time. Using contact details or identifications of others is not allowed and is considered fraud. We will deactivate your account at any time we identify your fraud.</p></div></div></div></div></div>',
    },
}
posts2_5 = {
    "type": "template_post",
    "lang_status": "True",
    "name": "Privacy Policy",
    "handle": "privacy-policy",
    "tran_name": {
        "source": "Privacy Policy",
        "tran": "Privacy Policy",
    },

    "tran_handle": {
        "source": "privacy-policy",
        "tran": "privacy-policy",
    },
    "content": {
        "source": '<div id="container" class="container pt-4"><div><div class="row"><div class="col-12 mx-auto col-xl-10"><div class="post-content"><h1 class="mb-4">Privacy Policy – Download Pinterest</h1><h2>Personal identification information</h2><p>Users may visit Pinterest Downloader App anonymously. We never record the identification information of our Users and will only collect personal identification information from Users if they voluntarily submit such information to us. Users can always refuse to supply personal identification information. However, if they agree to supply they are responsible for providing exact and correct identification information of themselves. Pinterest Downloader is not responsible for any fake or incorrect information provided by the Users. If we discover such incidents we would ban Users from accessing and using Pinterest Downloader App and our Services.</p><h2>Advertising</h2><p>We accept advertisements (Ads) on Pinterest Downloader App to maintain and support our own research and development on Pinterest Downloader App for non-commercial purposes. Ads appearing on Pinterest Downloader App may be delivered to Users by advertising partners who may set cookies. They will only compile non-personal identification information about you or others who use your computer and do not track personal information about you, such as your name, email address, and physical address. You may dismiss the use of the cookies or cease access to our application and website at any time as Users of Pinterest Downloader are not required to accept the Ads.</p><h2>Changes to this privacy policy</h2><p>Pinterest Downloader has the discretion to update this privacy policy at any time. When we do, we will post a notification on the main page of Pinterest Downloader App, revise the updated date on the top of this page. We encourage Users to frequently check this page for any changes to stay informed about how we are helping to protect the personal information we collect. You acknowledge and agree that it is your responsibility to review this privacy policy periodically and become aware of modifications.</p><h2>Your acceptance of these terms</h2><p>By accessing and using Pinterest Downloader App, you express your voluntary acceptance of this policy. If not, please do not use our Services. Your continued use of the Services following the posting of changes to this policy will be deemed your acceptance of those changes.</p></div></div></div></div></div>',

        "tran":  '<div id="container" class="container pt-4"><div><div class="row"><div class="col-12 mx-auto col-xl-10"><div class="post-content"><h1 class="mb-4">Privacy Policy – Download Pinterest</h1><h2>Personal identification information</h2><p>Users may visit Pinterest Downloader App anonymously. We never record the identification information of our Users and will only collect personal identification information from Users if they voluntarily submit such information to us. Users can always refuse to supply personal identification information. However, if they agree to supply they are responsible for providing exact and correct identification information of themselves. Pinterest Downloader is not responsible for any fake or incorrect information provided by the Users. If we discover such incidents we would ban Users from accessing and using Pinterest Downloader App and our Services.</p><h2>Advertising</h2><p>We accept advertisements (Ads) on Pinterest Downloader App to maintain and support our own research and development on Pinterest Downloader App for non-commercial purposes. Ads appearing on Pinterest Downloader App may be delivered to Users by advertising partners who may set cookies. They will only compile non-personal identification information about you or others who use your computer and do not track personal information about you, such as your name, email address, and physical address. You may dismiss the use of the cookies or cease access to our application and website at any time as Users of Pinterest Downloader are not required to accept the Ads.</p><h2>Changes to this privacy policy</h2><p>Pinterest Downloader has the discretion to update this privacy policy at any time. When we do, we will post a notification on the main page of Pinterest Downloader App, revise the updated date on the top of this page. We encourage Users to frequently check this page for any changes to stay informed about how we are helping to protect the personal information we collect. You acknowledge and agree that it is your responsibility to review this privacy policy periodically and become aware of modifications.</p><h2>Your acceptance of these terms</h2><p>By accessing and using Pinterest Downloader App, you express your voluntary acceptance of this policy. If not, please do not use our Services. Your continued use of the Services following the posting of changes to this policy will be deemed your acceptance of those changes.</p></div></div></div></div></div>',
    },
}



sknu_link = {
    "type": "template_menu",
    "lang_status": "True",
    "name": "header_menu",
    "content": {
        "menu_1":{
            "url": {
                "source": "about-us",
                "tran": "about-us",
            },
            "title": {
                "source": "About us - Pinterestdownloader.io",
                "tran": "About us - Pinterestdownloader.io",
            },
        },
        "menu_2":{

            "url": {
                "source": "contact",
                "tran": "contact",
            },
            "title": {
                "source": "Contact us - Pinterestdownloader.io",
                "tran": "Contact us - Pinterestdownloader.io",
            },    
        },
        "menu_3":{
            "url": {
                "source": "terms-conditions",
                "tran": "terms-conditions",
            },
            "title": {
                "source": "Terms and Conditions",
                "tran": "Terms and Conditions",
            },    
        },
        "menu_4":{
            "url": {
                "source": "privacy-policy",
                "tran": "privacy-policy",
            },
            "title": {
                "source": "Privacy Policy",
                "tran": "Privacy Policy",
            },    
        },
    },
}





list_lang = {
    "en": "English",
    "vi": "Việt Nam",
    "si": "Singapore",
    "cn": "China",
}