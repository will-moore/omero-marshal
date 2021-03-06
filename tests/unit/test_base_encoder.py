#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Glencoe Software, Inc. All rights reserved.
#
# This software is distributed under the terms described by the LICENCE file
# you can find at the root of the distribution bundle.
# If the file is missing please request a copy by contacting
# jason@glencoesoftware.com.
#

from omero_marshal import get_encoder


class TestBaseEncoder(object):

    def test_base_encoder(self, roi):
        encoder = get_encoder(roi.__class__)
        v = encoder.encode(roi)
        assert v == {
            '@id': 1L,
            '@type': 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#ROI',
            'Name': 'the_name',
            'Description': 'the_description',
            'omero:details': {
                '@type': 'TBD#Details',
                'group': {
                    '@id': 1L,
                    '@type':
                        'http://www.openmicroscopy.org/Schemas/OME/2015-01'
                        '#ExperimenterGroup',
                    'Description': 'the_description',
                    'Name': 'the_name',
                    'omero:details': {'@type': 'TBD#Details'}
                },
                'owner': {
                    '@id': 1L,
                    '@type':
                        'http://www.openmicroscopy.org/Schemas/OME/2015-01'
                        '#Experimenter',
                    'Email': 'the_email',
                    'FirstName': 'the_firstName',
                    'Institution': 'the_institution',
                    'LastName': 'the_lastName',
                    'MiddleName': 'the_middleName',
                    'UserName': 'the_omeName',
                    'omero:details': {'@type': 'TBD#Details'}
                },
                'permissions': {
                    '@type': 'TBD#Permissions',
                    'canAnnotate': True,
                    'canDelete': True,
                    'canEdit': True,
                    'canLink': True,
                    'perm': 'rwrwrw'
                }
            }
        }

    def test_base_encoder_with_unloaded_details_children(
            self, roi_with_unloaded_details_children):
        encoder = get_encoder(roi_with_unloaded_details_children.__class__)
        v = encoder.encode(roi_with_unloaded_details_children)
        assert v == {
            '@id': 1L,
            '@type': 'http://www.openmicroscopy.org/Schemas/ROI/2015-01#ROI',
            'Name': 'the_name',
            'Description': 'the_description',
            'omero:details': {
                '@type': 'TBD#Details',
                'owner': {
                    '@id': 1L,
                    '@type':
                        'http://www.openmicroscopy.org/Schemas/OME/2015-01'
                        '#Experimenter'
                },
                'group': {
                    '@id': 1L,
                    '@type':
                        'http://www.openmicroscopy.org/Schemas/OME/2015-01'
                        '#ExperimenterGroup'
                },
                'permissions': {
                    '@type': 'TBD#Permissions',
                    'canAnnotate': True,
                    'canDelete': True,
                    'canEdit': True,
                    'canLink': True,
                    'perm': 'rwrwrw'
                }
            }
        }


class TestDetailsEncoder(object):

    def experimenter_json(self):
        return {
            '@id': 1L,
            '@type':
                'http://www.openmicroscopy.org/Schemas/OME/2015-01'
                '#Experimenter',
            'FirstName': 'the_firstName',
            'MiddleName': 'the_middleName',
            'LastName': 'the_lastName',
            'Email': 'the_email',
            'Institution': 'the_institution',
            'UserName': 'the_omeName',
            'omero:details': {'@type': 'TBD#Details'}
        }

    def test_experimenter_encoder(self, experimenter):
        encoder = get_encoder(experimenter.__class__)
        v = encoder.encode(experimenter)
        assert v == self.experimenter_json()

    def experimenter_group_json(self):
        return {
            '@id': 1L,
            '@type':
                'http://www.openmicroscopy.org/Schemas/OME/2015-01'
                '#ExperimenterGroup',
            'Name': 'the_name',
            'Description': 'the_description',
            'omero:details': {'@type': 'TBD#Details'}
        }

    def test_experimenter_group_encoder(self, experimenter_group):
        encoder = get_encoder(experimenter_group.__class__)
        v = encoder.encode(experimenter_group)
        assert v == self.experimenter_group_json()

    def permissions_json(self):
        return {
            '@type': 'TBD#Permissions',
            'perm': 'rwrwrw',
            'canAnnotate': True,
            'canDelete': True,
            'canEdit': True,
            'canLink': True
        }

    def test_permissions_encoder(self, permissions):
        encoder = get_encoder(permissions.__class__)
        v = encoder.encode(permissions)
        assert v == self.permissions_json()

    def test_details_encoder(self, details):
        encoder = get_encoder(details.__class__)
        v = encoder.encode(details)
        assert v == {
            '@type': 'TBD#Details',
            'permissions': self.permissions_json(),
            'owner': self.experimenter_json(),
            'group': self.experimenter_group_json()
        }
