from cryptorg import Api

cryptorg = Api('API_KEY', 'API_SECRET');

""" First arg must be an array of parrams """
""" Second arg must be an array of attributes """

print(cryptorg.botList());
