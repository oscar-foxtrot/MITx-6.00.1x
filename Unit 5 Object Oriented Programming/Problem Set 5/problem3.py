class CiphertextMessage(Message):
    def __init__(self, text):
        """
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        Message.__init__(self, text)

    def decrypt_message(self):
        """
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        """
        max_val = 0
        best_shift = 0
        
        for i in range(len(string.ascii_lowercase)):
            idict = self.build_shift_dict(i)
            new_mes = self.apply_shift(i)
            wrd_list = new_mes.split(' ')
            counter = 0
            for wrd in wrd_list:
                if is_word(self.valid_words, wrd):
                    counter += 1
            if counter > max_val:
                max_val = counter
                best_shift = i
            
        decrypted_mes = self.apply_shift(best_shift)
        return best_shift, decrypted_mes
