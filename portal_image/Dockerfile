FROM centos
RUN curl -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py && rm -f get-pip.py && pip install django==1.11 djangorestframework mongoengine
CMD ["bash", "/portal_image/setup_portal.sh"]