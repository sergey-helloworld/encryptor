class EndsWithIVCipherDataPreparer:
        def split(self, cipher, iv_len):
            return {
                'body': cipher[:len(cipher)-iv_len],
                'iv': cipher[-iv_len:]
            }

        def join(self, body, iv):
            return body+iv