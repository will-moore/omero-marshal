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

from .. import Encoder
from omero.model import Annotation


class AnnotationEncoder(Encoder):
    '''
    Annotation
        BasicAnnotation
            BooleanAnnotation
                BooleanAnnotationI
            NumericAnnotation
                DoubleAnnotation
                    DoubleAnnotationI
                LongAnnotation
                    LongAnnotationI
            TermAnnotation
                TermAnnotationI
            TimestampAnnotation
                TimestampAnnotationI
        ListAnnotation
            ListAnnotationI
        MapAnnotation
            MapAnnotationI
        TextAnnotation
            CommentAnnotation
                CommentAnnotationI
            TagAnnotation
                TagAnnotationI
            XmlAnnotation
                XmlAnnotationI
        TypeAnnotation
            FileAnnotation
                FileAnnotationI
    '''

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01#Annotation'

    def encode(self, obj):
        v = super(AnnotationEncoder, self).encode(obj)
        self.set_if_not_none(v, 'Description', obj.description)
        self.set_if_not_none(v, 'Namespace', obj.ns)
        return v


class AnnotatableEncoder(Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01#AnnotationRef'

    def encode(self, obj):
        v = super(AnnotatableEncoder, self).encode(obj)
        if obj.isAnnotationLinksLoaded() and obj.sizeOfAnnotationLinks() > 0:
            annotations = list()
            for annotation_link in obj.copyAnnotationLinks():
                annotation = annotation_link.child
                annotation_encoder = self.ctx.get_encoder(annotation.__class__)
                annotations.append(
                    annotation_encoder.encode(annotation)
                )
            v['Annotations'] = annotations
        return v


encoder = (Annotation, AnnotationEncoder)
