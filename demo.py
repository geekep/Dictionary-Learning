import FeatureExtraction.process_cuboid as process_cuboid


def main():
    videosPath = './Train_vol'
    C3DfeaturesPath = './Train_feature'
    process_cuboid.main(videosPath, C3DfeaturesPath)
    videosPath = './Test_vol'
    C3DfeaturesPath = './Test_feature'
    process_cuboid.main(videosPath, C3DfeaturesPath)


if __name__ == '__main__':
    main()
