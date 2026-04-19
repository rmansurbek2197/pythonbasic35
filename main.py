class DictionarySwapper:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def swap_key_value(self):
        swapped_dict = {}
        for key, value in self.dictionary.items():
            if value not in swapped_dict:
                swapped_dict[value] = key
            else:
                print(f"Qiymat {value} allaqachon mavjud")
        return swapped_dict

    def print_original_dict(self):
        print("Original Dictionary:")
        for key, value in self.dictionary.items():
            print(f"{key}: {value}")

    def print_swapped_dict(self, swapped_dict):
        print("Swapped Dictionary:")
        for key, value in swapped_dict.items():
            print(f"{key}: {value}")

def main():
    dictionary = {"a": 1, "b": 2, "c": 3, "d": 4}
    swapper = DictionarySwapper(dictionary)
    swapper.print_original_dict()
    swapped_dict = swapper.swap_key_value()
    swapper.print_swapped_dict(swapped_dict)

    dictionary2 = {"apple": "red", "banana": "yellow", "cherry": "red"}
    swapper2 = DictionarySwapper(dictionary2)
    swapper2.print_original_dict()
    swapped_dict2 = swapper2.swap_key_value()
    swapper2.print_swapped_dict(swapped_dict2)

    dictionary3 = {"x": 10, "y": 20, "z": 30}
    swapper3 = DictionarySwapper(dictionary3)
    swapper3.print_original_dict()
    swapped_dict3 = swapper3.swap_key_value()
    swapper3.print_swapped_dict(swapped_dict3)

if __name__ == "__main__":
    main()