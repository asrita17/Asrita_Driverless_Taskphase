from setuptools import find_packages, setup

package_name = 'taskone_nodes'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='student@example.com',
    description='Task One publisher and subscriber',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'taskone_publisher = taskone_nodes.publisher:main',
            'taskone_subscriber = taskone_nodes.subscriber:main',
        ],
    },
)
