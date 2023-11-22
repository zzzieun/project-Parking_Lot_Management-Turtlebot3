from setuptools import setup

package_name = 'Bpro'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gus29',
    maintainer_email='gus29@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        
        'plate     = Bpro.plate:main',
        'scan      = Bpro.scan:main',
        'scan1      = Bpro.scan1:main',
        'scan2      = Bpro.scan2:main',
        
        'reg_params      = Bpro.reg_params:main',
       
        #--------------------------------------------------------
        'parking_lot1      = Bpro.parking_lot1:main',
        'parking_lot2      = Bpro.parking_lot2:main',
        'parking_lot3      = Bpro.parking_lot3:main',
        'parking_lot4      = Bpro.parking_lot4:main',
        'parking_lot5      = Bpro.parking_lot5:main',
        'parking_lot6      = Bpro.parking_lot6:main',
           
        'parking_lidar1    = Bpro.parking_lidar1:main',
        'parking_lidar2    = Bpro.parking_lidar2:main',
        'parking_lidar3    = Bpro.parking_lidar3:main',
        'parking_lidar4    = Bpro.parking_lidar4:main',
        'parking_lidar5    = Bpro.parking_lidar5:main',
        'parking_lidar6    = Bpro.parking_lidar6:main',
        
        'parking_marker1   = Bpro.parking_marker1:main',
        'parking_marker2   = Bpro.parking_marker2:main',
        'parking_marker3   = Bpro.parking_marker3:main',
        'parking_marker4   = Bpro.parking_marker4:main',
        'parking_marker5   = Bpro.parking_marker5:main',
        'parking_marker6   = Bpro.parking_marker6:main',
        
        'parking_plate1    = Bpro.parking_plate1:main',
        'parking_plate2    = Bpro.parking_plate2:main',
        'parking_plate3    = Bpro.parking_plate3:main',
        'parking_plate4    = Bpro.parking_plate4:main',
        'parking_plate5    = Bpro.parking_plate5:main',
        'parking_plate6    = Bpro.parking_plate6:main',
        
        ],
    },
)
