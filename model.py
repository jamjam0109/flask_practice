import argparse

def main(image_path):
    output = f"{image_path} -- execute mdodel !"
    print(output)

    return output

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_path', type=str)
    args = parser.parse_args()
    main(args.data_folder_path)
