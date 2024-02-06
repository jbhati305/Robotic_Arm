from setuptools import find_packages, setup

package_name = 'my_cam_scripts'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='amit',
    maintainer_email='amit@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'get_image=my_cam_scripts.get_image:main',
            'pub_image=my_cam_scripts.pub_image:main',
            'get_image_integrated=my_cam_scripts.get_image_integrated:main',
            'pub_image_try=my_cam_scripts.pub_image_try:main',
            'ros_to_arduino=my_cam_scripts.ros_to_arduino:main',
            'trial=my_cam_scripts.trial:main',
            'xyz_publisher=my_cam_scripts.xyz_publisher:main',
        ],
    },
)
