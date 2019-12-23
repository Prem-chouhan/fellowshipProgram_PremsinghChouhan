


def note_delete(self):
    print(self.path)
    if self.path == '/delete':
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        test_data = simplejson.loads(post_body)

        print("post_body(%s)" % test_data)
        json = test_data
        print(json)
        print(json['id'])

        id = json['id']
        delete_note(id)