from setuptools import find_packages, setup

package_name = 'palindrome_nodes'

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
    description='Palindrome checker nodes',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'string_publisher = palindrome_nodes.string_publisher:main',
            'palindrome_checker = palindrome_nodes.palindrome_checker:main',
            'result_processor = palindrome_nodes.result_processor:main',
        ],
    },
)
