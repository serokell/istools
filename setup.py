from setuptools import setup

setup(
    name="istools",
    packages=['istools'],
    entry_points={
        'console_scripts': [
            'istools-openvpn-auth=istools.openvpn_auth:main',
        ],
    }
)
