# Valle Real Estate
### This is a Django based app deployed on digital ocean. Which uses all Django built ins.
It has custom administration for staff and a dashboard for registerd users.
- Django 2
- Python 3
- Postgresql

.
├── README.md
├── accounts
│   |
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── contacts
│   |
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── listings
│   |
│   ├── admin.py
│   ├── apps.py
│   ├── choices.py
│   ├── migrations
│   │   
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── media
│   └── photos
│       └── 2019
│           └── 01
│               └── 21
│                   ├── home-1.jpg
│                   ├── home-2.jpg
│                   ├── home-3.jpg
│                   ├── home-4.jpg
│                   ├── home-5.jpg
│                   ├── home-6.jpg
│                   ├── home-inside-1.jpg
│                   ├── home-inside-1_3ZQfFIC.jpg
│                   ├── home-inside-1_NmWYcGL.jpg
│                   ├── home-inside-2.jpg
│                   ├── home-inside-2_51YBzjf.jpg
│                   ├── home-inside-2_hSNTdS0.jpg
│                   ├── home-inside-2_mF5AHua.jpg
│                   ├── home-inside-3.jpg
│                   ├── home-inside-3_igstlDR.jpg
│                   ├── home-inside-4.jpg
│                   ├── home-inside-4_HfODsbI.jpg
│                   ├── home-inside-4_Jus5xCC.jpg
│                   ├── home-inside-5.jpg
│                   ├── home-inside-5_CjHYz7R.jpg
│                   ├── home-inside-5_NIaf6gM.jpg
│                   ├── home-inside-6.jpg
│                   ├── home-inside-6_Faxxxq6.jpg
│                   ├── home-inside-6_c0akoqz.jpg
│                   ├── home-inside-6_ceMmZwm.jpg
│                   ├── jenny.jpg
│                   ├── kyle.jpg
│                   └── mark.jpg
├── pages
│   |
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── realtors
|   |
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │  
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── static
│   ├── admin
│   │   ├── css
│   │   │   ├── autocomplete.css
│   │   │   ├── base.css
│   │   │   ├── changelists.css
│   │   │   ├── dashboard.css
│   │   │   ├── fonts.css
│   │   │   ├── forms.css
│   │   │   ├── login.css
│   │   │   ├── responsive.css
│   │   │   ├── responsive_rtl.css
│   │   │   ├── rtl.css
│   │   │   ├── vendor
│   │   │   │   └── select2
│   │   │   │       ├── LICENSE-SELECT2.md
│   │   │   │       ├── select2.css
│   │   │   │       └── select2.min.css
│   │   │   └── widgets.css
│   │   ├── fonts
│   │   │   ├── LICENSE.txt
│   │   │   ├── README.txt
│   │   │   ├── Roboto-Bold-webfont.woff
│   │   │   ├── Roboto-Light-webfont.woff
│   │   │   └── Roboto-Regular-webfont.woff
│   │   ├── img
│   │   │   ├── LICENSE
│   │   │   ├── README.txt
│   │   │   ├── calendar-icons.svg
│   │   │   ├── gis
│   │   │   │   ├── move_vertex_off.svg
│   │   │   │   └── move_vertex_on.svg
│   │   │   ├── icon-addlink.svg
│   │   │   ├── icon-alert.svg
│   │   │   ├── icon-calendar.svg
│   │   │   ├── icon-changelink.svg
│   │   │   ├── icon-clock.svg
│   │   │   ├── icon-deletelink.svg
│   │   │   ├── icon-no.svg
│   │   │   ├── icon-unknown-alt.svg
│   │   │   ├── icon-unknown.svg
│   │   │   ├── icon-yes.svg
│   │   │   ├── inline-delete.svg
│   │   │   ├── search.svg
│   │   │   ├── selector-icons.svg
│   │   │   ├── sorting-icons.svg
│   │   │   ├── tooltag-add.svg
│   │   │   └── tooltag-arrowright.svg
│   │   └── js
│   │       ├── SelectBox.js
│   │       ├── SelectFilter2.js
│   │       ├── actions.js
│   │       ├── actions.min.js
│   │       ├── admin
│   │       │   ├── DateTimeShortcuts.js
│   │       │   └── RelatedObjectLookups.js
│   │       ├── autocomplete.js
│   │       ├── calendar.js
│   │       ├── cancel.js
│   │       ├── change_form.js
│   │       ├── collapse.js
│   │       ├── collapse.min.js
│   │       ├── core.js
│   │       ├── inlines.js
│   │       ├── inlines.min.js
│   │       ├── jquery.init.js
│   │       ├── popup_response.js
│   │       ├── prepopulate.js
│   │       ├── prepopulate.min.js
│   │       ├── prepopulate_init.js
│   │       ├── timeparse.js
│   │       ├── urlify.js
│   │       └── vendor
│   │           ├── jquery
│   │           │   ├── LICENSE-JQUERY.txt
│   │           │   ├── jquery.js
│   │           │   └── jquery.min.js
│   │           ├── select2
│   │           │   ├── LICENSE-SELECT2.md
│   │           │   ├── i18n
│   │           │   │   ├── ar.js
│   │           │   │   ├── az.js
│   │           │   │   ├── bg.js
│   │           │   │   ├── ca.js
│   │           │   │   ├── cs.js
│   │           │   │   ├── da.js
│   │           │   │   ├── de.js
│   │           │   │   ├── el.js
│   │           │   │   ├── en.js
│   │           │   │   ├── es.js
│   │           │   │   ├── et.js
│   │           │   │   ├── eu.js
│   │           │   │   ├── fa.js
│   │           │   │   ├── fi.js
│   │           │   │   ├── fr.js
│   │           │   │   ├── gl.js
│   │           │   │   ├── he.js
│   │           │   │   ├── hi.js
│   │           │   │   ├── hr.js
│   │           │   │   ├── hu.js
│   │           │   │   ├── id.js
│   │           │   │   ├── is.js
│   │           │   │   ├── it.js
│   │           │   │   ├── ja.js
│   │           │   │   ├── km.js
│   │           │   │   ├── ko.js
│   │           │   │   ├── lt.js
│   │           │   │   ├── lv.js
│   │           │   │   ├── mk.js
│   │           │   │   ├── ms.js
│   │           │   │   ├── nb.js
│   │           │   │   ├── nl.js
│   │           │   │   ├── pl.js
│   │           │   │   ├── pt-BR.js
│   │           │   │   ├── pt.js
│   │           │   │   ├── ro.js
│   │           │   │   ├── ru.js
│   │           │   │   ├── sk.js
│   │           │   │   ├── sr-Cyrl.js
│   │           │   │   ├── sr.js
│   │           │   │   ├── sv.js
│   │           │   │   ├── th.js
│   │           │   │   ├── tr.js
│   │           │   │   ├── uk.js
│   │           │   │   ├── vi.js
│   │           │   │   ├── zh-CN.js
│   │           │   │   └── zh-TW.js
│   │           │   ├── select2.full.js
│   │           │   └── select2.full.min.js
│   │           └── xregexp
│   │               ├── LICENSE-XREGEXP.txt
│   │               ├── xregexp.js
│   │               └── xregexp.min.js
│   ├── css
│   │   ├── admin.css
│   │   ├── all.css
│   │   ├── bootstrap.css
│   │   ├── lightbox.min.css
│   │   └── style.css
│   ├── img
│   │   ├── about.jpg
│   │   ├── building.jpg
│   │   ├── lightbox
│   │   │   ├── close.png
│   │   │   ├── loading.gif
│   │   │   ├── next.png
│   │   │   └── prev.png
│   │   ├── logo.png
│   │   ├── logo100.png
│   │   └── showcase.jpg
│   ├── js
│   │   ├── bootstrap.bundle.min.js
│   │   ├── jquery-3.3.1.min.js
│   │   ├── lightbox.min.js
│   │   └── main.js
│   └── webfonts
│       ├── fa-brands-400.eot
│       ├── fa-brands-400.svg
│       ├── fa-brands-400.ttf
│       ├── fa-brands-400.woff
│       ├── fa-brands-400.woff2
│       ├── fa-regular-400.eot
│       ├── fa-regular-400.svg
│       ├── fa-regular-400.ttf
│       ├── fa-regular-400.woff
│       ├── fa-regular-400.woff2
│       ├── fa-solid-900.eot
│       ├── fa-solid-900.svg
│       ├── fa-solid-900.ttf
│       ├── fa-solid-900.woff
│       └── fa-solid-900.woff2
├── templates
│   ├── accounts
│   │   ├── dashboard.html
│   │   ├── login.html
│   │   └── register.html
│   ├── admin
│   │   └── base_site.html
│   ├── base.html
│   ├── listings
│   │   ├── listing.html
│   │   ├── listings.html
│   │   └── search.html
│   ├── pages
│   │   ├── about.html
│   │   └── index.html
│   └── partials
│       ├── _alerts.html
│       ├── _footer.html
│       ├── _navbar.html
│       └── _topbar.html
└── valle_real_estate
    |
    ├── settings.py
    ├── static
    │   ├── css
    │   │   ├── admin.css
    │   │   ├── all.css
    │   │   ├── bootstrap.css
    │   │   ├── lightbox.min.css
    │   │   └── style.css
    │   ├── img
    │   │   ├── about.jpg
    │   │   ├── building.jpg
    │   │   ├── lightbox
    │   │   │   ├── close.png
    │   │   │   ├── loading.gif
    │   │   │   ├── next.png
    │   │   │   └── prev.png
    │   │   ├── logo.png
    │   │   ├── logo100.png
    │   │   └── showcase.jpg
    │   ├── js
    │   │   ├── bootstrap.bundle.min.js
    │   │   ├── jquery-3.3.1.min.js
    │   │   ├── lightbox.min.js
    │   │   └── main.js
    │   └── webfonts
    │       ├── fa-brands-400.eot
    │       ├── fa-brands-400.svg
    │       ├── fa-brands-400.ttf
    │       ├── fa-brands-400.woff
    │       ├── fa-brands-400.woff2
    │       ├── fa-regular-400.eot
    │       ├── fa-regular-400.svg
    │       ├── fa-regular-400.ttf
    │       ├── fa-regular-400.woff
    │       ├── fa-regular-400.woff2
    │       ├── fa-solid-900.eot
    │       ├── fa-solid-900.svg
    │       ├── fa-solid-900.ttf
    │       ├── fa-solid-900.woff
    │       └── fa-solid-900.woff2
    ├── urls.py
    └── wsgi.py