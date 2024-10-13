routes = [
        # Journal Routes
        {
            'Endpoint': '/journals/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a list of journals'
        },
        {
            'Endpoint': '/journals/<int:pk>/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single journal object'
        },
        {
            'Endpoint': '/journals/',
            'method': 'POST',
            'body': {'title': "", 'content': "", 'author': ""},
            'description': 'Creates a new journal with the data sent in the POST request'
        },
        {
            'Endpoint': '/journals/<int:pk>/',
            'method': 'PUT',
            'body': {'title': "", 'content': "", 'author': ""},
            'description': 'Updates an existing journal with the data sent in the PUT request'
        },
        {
            'Endpoint': '/journals/<int:pk>/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing journal'
        },

        # Volume Routes
        {
            'Endpoint': '/volumes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a list of volumes'
        },
        {
            'Endpoint': '/volumes/<int:pk>/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single volume object'
        },
        {
            'Endpoint': '/volumes/',
            'method': 'POST',
            'body': {'volume_number': "", 'journal': ""},
            'description': 'Creates a new volume with the data sent in the POST request'
        },
        {
            'Endpoint': '/volumes/<int:pk>/',
            'method': 'PUT',
            'body': {'volume_number': "", 'journal': ""},
            'description': 'Updates an existing volume with the data sent in the PUT request'
        },
        {
            'Endpoint': '/volumes/<int:pk>/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing volume'
        },

        # Issue Routes
        {
            'Endpoint': '/issues/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a list of issues'
        },
        {
            'Endpoint': '/issues/<int:pk>/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single issue object'
        },
        {
            'Endpoint': '/issues/',
            'method': 'POST',
            'body': {'issue_number': "", 'volume': ""},
            'description': 'Creates a new issue with the data sent in the POST request'
        },
        {
            'Endpoint': '/issues/<int:pk>/',
            'method': 'PUT',
            'body': {'issue_number': "", 'volume': ""},
            'description': 'Updates an existing issue with the data sent in the PUT request'
        },
        {
            'Endpoint': '/issues/<int:pk>/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing issue'
        },

        # Paper Routes
        {
            'Endpoint': '/papers/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a list of papers'
        },
        {
            'Endpoint': '/papers/<int:pk>/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single paper object'
        },
        {
            'Endpoint': '/papers/',
            'method': 'POST',
            'body': {'title': "", 'authors': "", 'issue': ""},
            'description': 'Creates a new paper with the data sent in the POST request'
        },
        {
            'Endpoint': '/papers/<int:pk>/',
            'method': 'PUT',
            'body': {'title': "", 'authors': "", 'issue': ""},
            'description': 'Updates an existing paper with the data sent in the PUT request'
        },
        {
            'Endpoint': '/papers/<int:pk>/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing paper'
        },

        # News Routes
        {
            'Endpoint': '/news/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a list of news'
        },
        {
            'Endpoint': '/news/<int:pk>/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single news object'
        },
        {
            'Endpoint': '/news/',
            'method': 'POST',
            'body': {'title': "", 'content': ""},
            'description': 'Creates a new news entry with the data sent in the POST request'
        },
        {
            'Endpoint': '/news/<int:pk>/',
            'method': 'PUT',
            'body': {'title': "", 'content': ""},
            'description': 'Updates an existing news entry with the data sent in the PUT request'
        },
        {
            'Endpoint': '/news/<int:pk>/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing news entry'
        },

        # HomeSlider Routes
        {
            'Endpoint': '/home-sliders/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a list of home sliders'
        },
        {
            'Endpoint': '/home-sliders/<int:pk>/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single home slider object'
        },
        {
            'Endpoint': '/home-sliders/',
            'method': 'POST',
            'body': {'image_url': "", 'description': ""},
            'description': 'Creates a new home slider with the data sent in the POST request'
        },
        {
            'Endpoint': '/home-sliders/<int:pk>/',
            'method': 'PUT',
            'body': {'image_url': "", 'description': ""},
            'description': 'Updates an existing home slider with the data sent in the PUT request'
        },
        {
            'Endpoint': '/home-sliders/<int:pk>/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing home slider'
        },

        # Submission Routes
        {
            'Endpoint': '/submissions/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a list of submissions'
        },
        {
            'Endpoint': '/submissions/<int:pk>/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single submission object'
        },
        {
            'Endpoint': '/submissions/',
            'method': 'POST',
            'body': {'title': "", 'content': "", 'author': ""},
            'description': 'Creates a new submission with the data sent in the POST request'
        },
        {
            'Endpoint': '/submissions/<int:pk>/',
            'method': 'PUT',
            'body': {'title': "", 'content': "", 'author': ""},
            'description': 'Updates an existing submission with the data sent in the PUT request'
        },
        {
            'Endpoint': '/submissions/<int:pk>/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing submission'
        },

        # Newsletter Routes
        {
            'Endpoint': '/newsletters/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a list of newsletters'
        },
        {
            'Endpoint': '/newsletters/<int:pk>/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single newsletter object'
        },
        {
            'Endpoint': '/newsletters/',
            'method': 'POST',
            'body': {'email': ""},
            'description': 'Creates a new newsletter subscription with the data sent in the POST request'
        },
        {
            'Endpoint': '/newsletters/<int:pk>/',
            'method': 'PUT',
            'body': {'email': ""},
            'description': 'Updates an existing newsletter subscription with the data sent in the PUT request'
        },
        {
            'Endpoint': '/newsletters/<int:pk>/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing newsletter subscription'
        },

        # About Routes
        {
            'Endpoint': '/about/',
            'method': 'GET',
            'body': None,
            'description': 'Returns information about the organization'
        },
        {
            'Endpoint': '/about/<int:pk>/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a specific about entry'
        },
        {
            'Endpoint': '/about/',
            'method': 'POST',
            'body': {'content': ""},
            'description': 'Creates a new about entry with the data sent in the POST request'
        },
        {
            'Endpoint': '/about/<int:pk>/',
            'method': 'PUT',
            'body': {'content': ""},
            'description': 'Updates an existing about entry with the data sent in the PUT request'
        },
        {
            'Endpoint': '/about/<int:pk>/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing about entry'
        },

        # Contact Routes
        {
            'Endpoint': '/contacts/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a list of contacts'
        },
        {
            'Endpoint': '/contacts/<int:pk>/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single contact object'
        },
        {
            'Endpoint': '/contacts/',
            'method': 'POST',
            'body': {'name': "", 'email': "", 'message': ""},
            'description': 'Creates a new contact entry with the data sent in the POST request'
        },
        {
            'Endpoint': '/contacts/<int:pk>/',
            'method': 'PUT',
            'body': {'name': "", 'email': "", 'message': ""},
            'description': 'Updates an existing contact entry with the data sent in the PUT request'
        },
        {
            'Endpoint': '/contacts/<int:pk>/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing contact entry'
        },

        # Author Routes
        {
            'Endpoint': '/authors/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a list of authors'
        },
        {
            'Endpoint': '/authors/<int:pk>/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single author object'
        },
        {
            'Endpoint': '/authors/',
            'method': 'POST',
            'body': {'name': "", 'affiliation': ""},
            'description': 'Creates a new author with the data sent in the POST request'
        },
        {
            'Endpoint': '/authors/<int:pk>/',
            'method': 'PUT',
            'body': {'name': "", 'affiliation': ""},
            'description': 'Updates an existing author with the data sent in the PUT request'
        },
        {
            'Endpoint': '/authors/<int:pk>/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing author'
        },

        # Reviewer Routes
        {
            'Endpoint': '/reviewers/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a list of reviewers'
        },
        {
            'Endpoint': '/reviewers/<int:pk>/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single reviewer object'
        },
        {
            'Endpoint': '/reviewers/',
            'method': 'POST',
            'body': {'name': "", 'expertise': ""},
            'description': 'Creates a new reviewer with the data sent in the POST request'
        },
        {
            'Endpoint': '/reviewers/<int:pk>/',
            'method': 'PUT',
            'body': {'name': "", 'expertise': ""},
            'description': 'Updates an existing reviewer with the data sent in the PUT request'
        },
        {
            'Endpoint': '/reviewers/<int:pk>/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing reviewer'
        },

        # Editor Routes
        {
            'Endpoint': '/editors/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a list of editors'
        },
        {
            'Endpoint': '/editors/<int:pk>/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single editor object'
        },
        {
            'Endpoint': '/editors/',
            'method': 'POST',
            'body': {'name': "", 'department': ""},
            'description': 'Creates a new editor with the data sent in the POST request'
        },
        {
            'Endpoint': '/editors/<int:pk>/',
            'method': 'PUT',
            'body': {'name': "", 'department': ""},
            'description': 'Updates an existing editor with the data sent in the PUT request'
        },
    ]